# Generated by Django 3.0.3 on 2020-02-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.CharField(blank=True, choices=[('A', 'Ativo(a)'), ('I', 'Inativo(a)')], default='I', max_length=1, verbose_name='Status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Endereço de E-mail')),
                ('name', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone')),
                ('type_user', models.CharField(choices=[('P', 'Paciente'), ('M', 'Médico/Psicólogo')], max_length=1, verbose_name='Tipo de usuário')),
                ('state', models.CharField(blank=True, default='PI', max_length=100, verbose_name='Estado')),
                ('city', models.CharField(blank=True, default='Teresina', max_length=100, verbose_name='Cidade')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='É da equipe?')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['name'],
            },
        ),
    ]
