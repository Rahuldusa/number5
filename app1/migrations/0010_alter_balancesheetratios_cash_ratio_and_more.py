# Generated by Django 5.0.6 on 2024-10-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_company_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancesheetratios',
            name='cash_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='current_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='debt_capital_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='debt_equity_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='debt_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='debt_service_coverage_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='equity_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='operating_cash_flow_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='quick_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='balancesheetratios',
            name='working_capital',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='cash_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='current_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='debt_service_coverage_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='operating_cash_flow_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='quick_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cashflowratios',
            name='working_capital',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='debt_service_coverage_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='earnings_per_share',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='ebitda_margin',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='gross_profit_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='interest_service',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='net_profit_margin',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='operating_cash_flow_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatementratios',
            name='operating_profit_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
    ]
