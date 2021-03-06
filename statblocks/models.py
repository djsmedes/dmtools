from random import randint
from dal import autocomplete
from django.db import models
from django.forms import ModelForm

from multiselectfield import MultiSelectField

from base.models import BaseModel
from base.utils import Size, Alignment, Die, DamageType, Condition, Language, AbilityScore


class Monster(BaseModel):
    generic_name = models.CharField(max_length=255, null=True, blank=True,
                                    help_text="If not specified, the name in lowercase will be used.")
    size = models.IntegerField(choices=Size.MODEL_CHOICES, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    alignment = models.IntegerField(choices=Alignment.MODEL_CHOICES, null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    armor_kind = models.CharField(max_length=255, null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    num_hit_die = models.IntegerField(null=True, blank=True)
    hit_die_size = models.IntegerField(choices=Die.MODEL_CHOICES, null=True, blank=True)
    speed = models.CharField(max_length=100, null=True, blank=True)
    str = models.IntegerField(null=True, blank=True)
    dex = models.IntegerField(null=True, blank=True)
    con = models.IntegerField(null=True, blank=True)
    int = models.IntegerField(null=True, blank=True)
    wis = models.IntegerField(null=True, blank=True)
    cha = models.IntegerField(null=True, blank=True)
    proficiency = models.IntegerField(null=True, blank=True)

    @property
    def str_mod(self):
        if self.str:
            return (self.str - 10) // 2
        else:
            return -5

    @property
    def dex_mod(self):
        if self.dex:
            return (self.dex - 10) // 2
        else:
            return -5

    @property
    def con_mod(self):
        if self.con:
            return (self.con - 10) // 2
        else:
            return -5

    @property
    def int_mod(self):
        if self.int:
            return (self.int - 10) // 2
        else:
            return -5

    @property
    def wis_mod(self):
        if self.wis:
            return (self.wis - 10) // 2
        else:
            return -5

    @property
    def cha_mod(self):
        if self.cha:
            return (self.cha - 10) // 2
        else:
            return -5

    saving_throws = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    damage_vulnerabilities = MultiSelectField(choices=DamageType.MODEL_CHOICES, null=True, blank=True)
    damage_resistances = MultiSelectField(choices=DamageType.MODEL_CHOICES, null=True, blank=True)
    damage_immunities = MultiSelectField(choices=DamageType.MODEL_CHOICES, null=True, blank=True)
    condition_immunities = MultiSelectField(choices=Condition.MODEL_CHOICES, null=True, blank=True)
    senses = models.CharField(max_length=255, null=True, blank=True)
    languages = MultiSelectField(choices=Language.MODEL_CHOICES, null=True, blank=True)
    challenge = models.CharField(
        max_length=3,
        choices=[
            '0', '1/8', '1/4', '1/2'
        ].extend(['{}'.format(num) for num in range(1, 31)]),
        null=True, blank=True
    )

    special_properties = models.ManyToManyField('statblocks.SpecialProperty', blank=True)
    actions = models.ManyToManyField('statblocks.Action', blank=True)
    legendary_actions = models.ManyToManyField('statblocks.LegendaryAction', blank=True)
    reactions = models.ManyToManyField('statblocks.Reaction', blank=True)

    @property
    def rand_hp(self):
        hp = 0
        for _ in range(self.num_hit_die):
            hp += max(randint(1, self.hit_die_size) + self.con_mod, 1)
        return hp

    @property
    def avg_hp(self):
        con_mod_piece = self.num_hit_die * self.con_mod
        hit_die_avg = (self.hit_die_size + 1) / 2.0
        hit_die_piece = self.num_hit_die * hit_die_avg // 1
        return max(int(con_mod_piece + hit_die_piece), 1)

    @property
    def statblock_generic_name(self):
        if self.generic_name:
            return self.generic_name
        else:
            return self.name.lower()


class StatblockBit(BaseModel):
    class Meta:
        abstract = True

    statblock_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sort_priority = models.IntegerField(default=0)
    save_dc = models.IntegerField(null=True, blank=True)
    save_type = models.CharField(max_length=3, choices=AbilityScore.MODEL_CHOICES, null=True, blank=True)

    @property
    def title(self):
        if self.statblock_title:
            return self.statblock_title
        else:
            return self.name

    @property
    def monsters_with(self):
        if hasattr(self, 'monster_set'):
            return str(len(self.monster_set.all()))
        else:
            return '0'


class SpecialProperty(StatblockBit):
    class Meta:
        ordering = ['-sort_priority']


class Action(StatblockBit):

    MELEE_WEAPON_ATTACK = 1
    RANGED_WEAPON_ATTACK = 2
    MELEE_SPELL_ATTACK = 3
    RANGED_SPELL_ATTACK = 4
    ATTACK_TYPE_CHOICES = [
        (MELEE_WEAPON_ATTACK, 'melee weapon attack'),
        (RANGED_WEAPON_ATTACK, 'ranged weapon attack'),
        (MELEE_SPELL_ATTACK, 'melee spell attack'),
        (RANGED_SPELL_ATTACK, 'ranged spell attack'),
    ]

    attack_type = models.IntegerField(choices=ATTACK_TYPE_CHOICES, null=True, blank=True)
    attack_uses = models.CharField(max_length=3, choices=AbilityScore.MODEL_CHOICES, null=True, blank=True, verbose_name='ability score used')
    attack_tohit_bonus_override = models.IntegerField(null=True, blank=True, verbose_name='to-hit bonus')
    reach_range = models.IntegerField(choices=[(5 * num, '{} ft.'.format(5 * num)) for num in range(120)], null=True,
                                      blank=True, verbose_name='reach or first range increment')
    range_secondary = models.IntegerField(choices=[(5 * num, '{} ft.'.format(5 * num)) for num in range(120)],
                                          null=True, blank=True, verbose_name='second range increment')
    num_targets = models.IntegerField(null=True, blank=True, verbose_name='number of targets')
    hit_num_damage_dice = models.IntegerField(null=True, blank=True, verbose_name='number of damage dice')
    hit_type_damage_dice = models.IntegerField(choices=Die.MODEL_CHOICES, null=True, blank=True, verbose_name='damage die')
    hit_damage_type = models.IntegerField(choices=DamageType.MODEL_CHOICES, null=True, blank=True, verbose_name='damage type')
    hit_addl_num_damage_dice = models.IntegerField(null=True, blank=True, verbose_name='number of damage dice (secondary)')
    hit_addl_type_damage_dice = models.IntegerField(choices=Die.MODEL_CHOICES, null=True, blank=True, verbose_name='damage die (secondary)')
    hit_addl_damage_type = models.IntegerField(choices=DamageType.MODEL_CHOICES, null=True, blank=True, verbose_name='damage type (secondary)')

    class Meta:
        ordering = ['-sort_priority']


class LegendaryAction(StatblockBit):
    class Meta:
        ordering = ['-sort_priority']


class Reaction(StatblockBit):
    class Meta:
        ordering = ['-sort_priority']


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'
        widgets = {
            'special_properties': autocomplete.ModelSelect2Multiple(url='specialproperty-autocomplete'),
            'actions': autocomplete.ModelSelect2Multiple(url='action-autocomplete'),
            'legendary_actions': autocomplete.ModelSelect2Multiple(url='legendaryaction-autocomplete'),
            'reactions': autocomplete.ModelSelect2Multiple(url='reaction-autocomplete'),
        }


class SpecialPropertyForm(ModelForm):
    class Meta:
        model = SpecialProperty
        fields = '__all__'


class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = '__all__'


class LegendaryActionForm(ModelForm):
    class Meta:
        model = LegendaryAction
        fields = '__all__'


class ReactionForm(ModelForm):
    class Meta:
        model = Reaction
        fields = '__all__'
