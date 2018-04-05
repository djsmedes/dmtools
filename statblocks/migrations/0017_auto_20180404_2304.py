# Generated by Django 2.0 on 2018-04-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statblocks', '0016_auto_20180404_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='attack_tohit_bonus_override',
            field=models.IntegerField(blank=True, null=True, verbose_name='to-hit bonus'),
        ),
        migrations.AlterField(
            model_name='action',
            name='attack_uses',
            field=models.CharField(blank=True, choices=[('str', 'strength'), ('dex', 'dexterity'), ('con', 'constitution'), ('int', 'intelligence'), ('wis', 'wisdom'), ('cha', 'charisma')], max_length=3, null=True, verbose_name='ability score used'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_addl_damage_type',
            field=models.IntegerField(blank=True, choices=[(1, 'bludgeoning'), (2, 'piercing'), (3, 'slashing'), (4, 'bludgeoning, piercing, and slashing'), (5, 'bludgeoning, piercing, and slashing from nonmagical attacks'), (6, 'bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons'), (7, 'fire'), (8, 'cold'), (9, 'acid'), (10, 'lightning'), (11, 'thunder'), (12, 'poison'), (13, 'psychic'), (14, 'force'), (15, 'radiant'), (16, 'necrotic')], null=True, verbose_name='damage type (secondary)'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_addl_num_damage_dice',
            field=models.IntegerField(blank=True, null=True, verbose_name='number of damage dice (secondary)'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_addl_type_damage_dice',
            field=models.IntegerField(blank=True, choices=[(4, 'd4'), (6, 'd6'), (8, 'd8'), (10, 'd10'), (12, 'd12'), (20, 'd20'), (100, 'd100')], null=True, verbose_name='damage die (secondary)'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_damage_type',
            field=models.IntegerField(blank=True, choices=[(1, 'bludgeoning'), (2, 'piercing'), (3, 'slashing'), (4, 'bludgeoning, piercing, and slashing'), (5, 'bludgeoning, piercing, and slashing from nonmagical attacks'), (6, 'bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons'), (7, 'fire'), (8, 'cold'), (9, 'acid'), (10, 'lightning'), (11, 'thunder'), (12, 'poison'), (13, 'psychic'), (14, 'force'), (15, 'radiant'), (16, 'necrotic')], null=True, verbose_name='damage type'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_num_damage_dice',
            field=models.IntegerField(blank=True, null=True, verbose_name='number of damage dice'),
        ),
        migrations.AlterField(
            model_name='action',
            name='hit_type_damage_dice',
            field=models.IntegerField(blank=True, choices=[(4, 'd4'), (6, 'd6'), (8, 'd8'), (10, 'd10'), (12, 'd12'), (20, 'd20'), (100, 'd100')], null=True, verbose_name='damage die'),
        ),
        migrations.AlterField(
            model_name='action',
            name='num_targets',
            field=models.IntegerField(blank=True, null=True, verbose_name='number of targets'),
        ),
        migrations.AlterField(
            model_name='action',
            name='range_secondary',
            field=models.IntegerField(blank=True, choices=[(0, '0 ft.'), (5, '5 ft.'), (10, '10 ft.'), (15, '15 ft.'), (20, '20 ft.'), (25, '25 ft.'), (30, '30 ft.'), (35, '35 ft.'), (40, '40 ft.'), (45, '45 ft.'), (50, '50 ft.'), (55, '55 ft.'), (60, '60 ft.'), (65, '65 ft.'), (70, '70 ft.'), (75, '75 ft.'), (80, '80 ft.'), (85, '85 ft.'), (90, '90 ft.'), (95, '95 ft.'), (100, '100 ft.'), (105, '105 ft.'), (110, '110 ft.'), (115, '115 ft.'), (120, '120 ft.'), (125, '125 ft.'), (130, '130 ft.'), (135, '135 ft.'), (140, '140 ft.'), (145, '145 ft.'), (150, '150 ft.'), (155, '155 ft.'), (160, '160 ft.'), (165, '165 ft.'), (170, '170 ft.'), (175, '175 ft.'), (180, '180 ft.'), (185, '185 ft.'), (190, '190 ft.'), (195, '195 ft.'), (200, '200 ft.'), (205, '205 ft.'), (210, '210 ft.'), (215, '215 ft.'), (220, '220 ft.'), (225, '225 ft.'), (230, '230 ft.'), (235, '235 ft.'), (240, '240 ft.'), (245, '245 ft.'), (250, '250 ft.'), (255, '255 ft.'), (260, '260 ft.'), (265, '265 ft.'), (270, '270 ft.'), (275, '275 ft.'), (280, '280 ft.'), (285, '285 ft.'), (290, '290 ft.'), (295, '295 ft.'), (300, '300 ft.'), (305, '305 ft.'), (310, '310 ft.'), (315, '315 ft.'), (320, '320 ft.'), (325, '325 ft.'), (330, '330 ft.'), (335, '335 ft.'), (340, '340 ft.'), (345, '345 ft.'), (350, '350 ft.'), (355, '355 ft.'), (360, '360 ft.'), (365, '365 ft.'), (370, '370 ft.'), (375, '375 ft.'), (380, '380 ft.'), (385, '385 ft.'), (390, '390 ft.'), (395, '395 ft.'), (400, '400 ft.'), (405, '405 ft.'), (410, '410 ft.'), (415, '415 ft.'), (420, '420 ft.'), (425, '425 ft.'), (430, '430 ft.'), (435, '435 ft.'), (440, '440 ft.'), (445, '445 ft.'), (450, '450 ft.'), (455, '455 ft.'), (460, '460 ft.'), (465, '465 ft.'), (470, '470 ft.'), (475, '475 ft.'), (480, '480 ft.'), (485, '485 ft.'), (490, '490 ft.'), (495, '495 ft.'), (500, '500 ft.'), (505, '505 ft.'), (510, '510 ft.'), (515, '515 ft.'), (520, '520 ft.'), (525, '525 ft.'), (530, '530 ft.'), (535, '535 ft.'), (540, '540 ft.'), (545, '545 ft.'), (550, '550 ft.'), (555, '555 ft.'), (560, '560 ft.'), (565, '565 ft.'), (570, '570 ft.'), (575, '575 ft.'), (580, '580 ft.'), (585, '585 ft.'), (590, '590 ft.'), (595, '595 ft.')], null=True, verbose_name='second range increment'),
        ),
        migrations.AlterField(
            model_name='action',
            name='reach_range',
            field=models.IntegerField(blank=True, choices=[(0, '0 ft.'), (5, '5 ft.'), (10, '10 ft.'), (15, '15 ft.'), (20, '20 ft.'), (25, '25 ft.'), (30, '30 ft.'), (35, '35 ft.'), (40, '40 ft.'), (45, '45 ft.'), (50, '50 ft.'), (55, '55 ft.'), (60, '60 ft.'), (65, '65 ft.'), (70, '70 ft.'), (75, '75 ft.'), (80, '80 ft.'), (85, '85 ft.'), (90, '90 ft.'), (95, '95 ft.'), (100, '100 ft.'), (105, '105 ft.'), (110, '110 ft.'), (115, '115 ft.'), (120, '120 ft.'), (125, '125 ft.'), (130, '130 ft.'), (135, '135 ft.'), (140, '140 ft.'), (145, '145 ft.'), (150, '150 ft.'), (155, '155 ft.'), (160, '160 ft.'), (165, '165 ft.'), (170, '170 ft.'), (175, '175 ft.'), (180, '180 ft.'), (185, '185 ft.'), (190, '190 ft.'), (195, '195 ft.'), (200, '200 ft.'), (205, '205 ft.'), (210, '210 ft.'), (215, '215 ft.'), (220, '220 ft.'), (225, '225 ft.'), (230, '230 ft.'), (235, '235 ft.'), (240, '240 ft.'), (245, '245 ft.'), (250, '250 ft.'), (255, '255 ft.'), (260, '260 ft.'), (265, '265 ft.'), (270, '270 ft.'), (275, '275 ft.'), (280, '280 ft.'), (285, '285 ft.'), (290, '290 ft.'), (295, '295 ft.'), (300, '300 ft.'), (305, '305 ft.'), (310, '310 ft.'), (315, '315 ft.'), (320, '320 ft.'), (325, '325 ft.'), (330, '330 ft.'), (335, '335 ft.'), (340, '340 ft.'), (345, '345 ft.'), (350, '350 ft.'), (355, '355 ft.'), (360, '360 ft.'), (365, '365 ft.'), (370, '370 ft.'), (375, '375 ft.'), (380, '380 ft.'), (385, '385 ft.'), (390, '390 ft.'), (395, '395 ft.'), (400, '400 ft.'), (405, '405 ft.'), (410, '410 ft.'), (415, '415 ft.'), (420, '420 ft.'), (425, '425 ft.'), (430, '430 ft.'), (435, '435 ft.'), (440, '440 ft.'), (445, '445 ft.'), (450, '450 ft.'), (455, '455 ft.'), (460, '460 ft.'), (465, '465 ft.'), (470, '470 ft.'), (475, '475 ft.'), (480, '480 ft.'), (485, '485 ft.'), (490, '490 ft.'), (495, '495 ft.'), (500, '500 ft.'), (505, '505 ft.'), (510, '510 ft.'), (515, '515 ft.'), (520, '520 ft.'), (525, '525 ft.'), (530, '530 ft.'), (535, '535 ft.'), (540, '540 ft.'), (545, '545 ft.'), (550, '550 ft.'), (555, '555 ft.'), (560, '560 ft.'), (565, '565 ft.'), (570, '570 ft.'), (575, '575 ft.'), (580, '580 ft.'), (585, '585 ft.'), (590, '590 ft.'), (595, '595 ft.')], null=True, verbose_name='reach or first range increment'),
        ),
    ]