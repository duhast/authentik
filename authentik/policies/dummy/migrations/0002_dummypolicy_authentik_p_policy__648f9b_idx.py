# Generated by Django 4.1.2 on 2022-10-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_policies_dummy", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="dummypolicy",
            index=models.Index(fields=["policy_ptr_id"], name="authentik_p_policy__648f9b_idx"),
        ),
    ]
