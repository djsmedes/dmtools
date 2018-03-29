# Generated by Django 2.0 on 2018-03-29 16:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('statblocks', '0002_auto_20180329_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='alignment',
            field=models.IntegerField(blank=True, choices=[(1, 'Lawful good'), (2, 'Neutral good'), (3, 'Chaotic good'), (4, 'Lawful neutral'), (5, 'Neutral'), (6, 'Chaotic neutral'), (7, 'Lawful evil'), (8, 'Neutral evil'), (9, 'Chaotic evil')], null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='armor_class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='armor_kind',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='cha',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='challenge',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='con',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='condition_immunities',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'blinded'), (2, 'charmed'), (3, 'deafened'), (4, 'frightened'), (5, 'grappled'), (6, 'incapacitated'), (7, 'invisible'), (8, 'paralyzed'), (9, 'petrified'), (10, 'poisoned'), (11, 'prone'), (12, 'restrained'), (13, 'stunned'), (14, 'unconscious')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='damage_immunities',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'bludgeoning'), (2, 'piercing'), (3, 'slashing'), (4, 'bludgeoning, piercing, and slashing'), (5, 'bludgeoning, piercing, and slashing from nonmagical attacks'), (6, 'bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons'), (7, 'fire'), (8, 'cold'), (9, 'acid'), (10, 'lightning'), (11, 'thunder'), (12, 'poison'), (13, 'psychic'), (14, 'force'), (15, 'radiant'), (16, 'necrotic')], max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='damage_resistances',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'bludgeoning'), (2, 'piercing'), (3, 'slashing'), (4, 'bludgeoning, piercing, and slashing'), (5, 'bludgeoning, piercing, and slashing from nonmagical attacks'), (6, 'bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons'), (7, 'fire'), (8, 'cold'), (9, 'acid'), (10, 'lightning'), (11, 'thunder'), (12, 'poison'), (13, 'psychic'), (14, 'force'), (15, 'radiant'), (16, 'necrotic')], max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='damage_vulnerabilities',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'bludgeoning'), (2, 'piercing'), (3, 'slashing'), (4, 'bludgeoning, piercing, and slashing'), (5, 'bludgeoning, piercing, and slashing from nonmagical attacks'), (6, 'bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons'), (7, 'fire'), (8, 'cold'), (9, 'acid'), (10, 'lightning'), (11, 'thunder'), (12, 'poison'), (13, 'psychic'), (14, 'force'), (15, 'radiant'), (16, 'necrotic')], max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='dex',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='hit_die_size',
            field=models.IntegerField(blank=True, choices=[(4, 'd4'), (6, 'd6'), (8, 'd8'), (10, 'd10'), (12, 'd12'), (20, 'd20'), (100, 'd100')], null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='hit_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='int',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='languages',
            field=models.IntegerField(blank=True, choices=[(1, 'Common'), (2, 'Dwarvish'), (3, 'Elvish'), (4, 'Giant'), (5, 'Goblin'), (6, 'Orc'), (7, 'Gnomish'), (8, 'Halfling'), (9, 'Abyssal'), (10, 'Celestial'), (11, 'Infernal'), (12, 'Draconic'), (13, 'Sylvan'), (14, 'Primordial'), (15, 'Auran'), (16, 'Aquan'), (17, 'Ignan'), (18, 'Terran'), (19, 'Undercommon'), (20, 'Deep Speech'), (21, 'Druidic'), (22, "Thieve's Cant")], null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='num_hit_die',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='saving_throws',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='senses',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='size',
            field=models.IntegerField(blank=True, choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Huge'), (6, 'Gargantuan'), (7, 'Colossal')], null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='skills',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='speed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='str',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='wis',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
