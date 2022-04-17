# Generated by Django 4.0.3 on 2022-04-12 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("guild", "0003_alter_guildmember_guild_alter_teammember_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="guildteam",
            name="guild",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                to="guild.guild",
                verbose_name="Guild",
            ),
            preserve_default=False,
        ),
    ]