# -*- coding: utf-8 -*-
from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import tendenci.libs.tinymce.models
import tendenci.apps.base.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberships', '0001_initial'),
        ('industries', '0001_initial'),
        ('events', '0001_initial'),
        ('entities', '0001_initial'),
        ('invoices', '0001_initial'),
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('renewal', models.BooleanField(default=False)),
                ('renew_dt', models.DateTimeField(null=True, verbose_name='Renew Date Time')),
                ('join_dt', models.DateTimeField(verbose_name='Join Date Time')),
                ('expiration_dt', models.DateTimeField(null=True, verbose_name='Expiration Date Time', blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('approved_denied_dt', models.DateTimeField(null=True, verbose_name='Approved or Denied Date Time')),
                ('admin_notes', models.TextField(null=True, verbose_name='Admin notes', blank=True)),
                ('total_passes_allowed', models.PositiveIntegerField(default=0, verbose_name='Total Passes Allowed', blank=True)),
            ],
            options={
                'verbose_name': 'Corporate Member',
                'verbose_name_plural': 'Corporate Members',
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=155, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=155, verbose_name='URL Path')),
                ('authentication_method', models.CharField(default='admin', help_text='Define a method for individuals to be bound to their corporate memberships when signing up.', max_length=50, verbose_name='Authentication Method', choices=[('admin', 'Admin Approval'), ('email', 'E-mail Domain'), ('secret_code', 'Secret Code')])),
                ('description', tendenci.libs.tinymce.models.HTMLField(help_text='Will display at the top of the application form.', null=True, verbose_name='Description', blank=True)),
                ('notes', models.TextField(help_text='Notes for editor. Will not display on the application form.', null=True, verbose_name='Notes', blank=True)),
                ('confirmation_text', models.TextField(null=True, verbose_name='Confirmation Text', blank=True)),
                ('include_tax', models.BooleanField(default=False)),
                ('tax_rate', models.DecimalField(default=0, help_text='Example: 0.0825 for 8.25%.', max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Corporate Membership Application',
                'verbose_name_plural': 'Corporate Membership Applications',
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipAppField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=0, null=True, verbose_name='Position', blank=True)),
                ('label', models.CharField(max_length=2000, verbose_name='Label')),
                ('field_name', models.CharField(default='', max_length=30, verbose_name='Field Name', blank=True)),
                ('field_type', models.CharField(default='CharField', choices=[('CharField', 'Text'), ('CharField/django.forms.Textarea', 'Paragraph Text'), ('BooleanField', 'Checkbox'), ('ChoiceField', 'Select One from a list (Drop Down)'), ('ChoiceField/django.forms.RadioSelect', 'Select One from a list (Radio Buttons)'), ('MultipleChoiceField', 'Multi select (Drop Down)'), ('MultipleChoiceField/django.forms.CheckboxSelectMultiple', 'Multi select (Checkboxes)'), ('CountrySelectField', 'Countries Drop Down'), ('EmailField', 'Email'), ('FileField', 'File upload'), ('DateField/django.forms.widgets.SelectDateWidget', 'Date'), ('DateTimeField', 'Date/time'), ('section_break', 'Section Break')], max_length=80, blank=True, null=True, verbose_name='Field Type')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('display', models.BooleanField(default=True, verbose_name='Show')),
                ('admin_only', models.BooleanField(default=False, verbose_name='Admin Only')),
                ('help_text', models.CharField(default='', max_length=2000, verbose_name='Help Text', blank=True)),
                ('choices', models.CharField(help_text='Comma separated options where applicable', max_length=1000, null=True, verbose_name='Choices', blank=True)),
                ('field_layout', models.CharField(default='1', choices=[('1', 'One Column'), ('2', 'Two Columns'), ('3', 'Three Columns'), ('0', 'Side by Side')], max_length=50, blank=True, null=True, verbose_name='Choice Field Layout')),
                ('size', models.CharField(default='m', choices=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], max_length=1, blank=True, null=True, verbose_name='Field Size')),
                ('default_value', models.CharField(default='', max_length=100, verbose_name='Default Value', blank=True)),
                ('css_class', models.CharField(default='', max_length=50, verbose_name='CSS Class Name', blank=True)),
                ('description', models.TextField(default='', max_length=200, verbose_name='Description', blank=True)),
                ('corp_app', models.ForeignKey(related_name='fields', to='corporate_memberships.CorpMembershipApp', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ('position',),
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipAuthDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_file', models.FileField(upload_to='imports/corpmemberships/093aeb8a', max_length=260, verbose_name='Upload File')),
                ('override', models.IntegerField(default=0, choices=[(0, 'Blank Fields'), (1, 'All Fields (override)')])),
                ('key', models.CharField(default='name', max_length=50, verbose_name='Key')),
                ('bind_members', models.BooleanField(default=False, verbose_name='Bind members to corporations by their company names')),
                ('total_rows', models.IntegerField(default=0)),
                ('num_processed', models.IntegerField(default=0)),
                ('summary', models.CharField(default='', max_length=500, null=True, verbose_name='Summary')),
                ('status', models.CharField(default='not_started', max_length=50, choices=[('not_started', 'Not Started'), ('preprocessing', 'Pre_processing'), ('preprocess_done', 'Pre_process Done'), ('processing', 'Processing'), ('completed', 'Completed')])),
                ('complete_dt', models.DateTimeField(null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipImportData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row_data', tendenci.apps.base.fields.DictField(verbose_name='Row Data')),
                ('row_num', models.IntegerField(verbose_name='Row #')),
                ('action_taken', models.CharField(max_length=20, null=True, verbose_name='Action Taken')),
                ('mimport', models.ForeignKey(related_name='corp_membership_import_data', to='corporate_memberships.CorpMembershipImport', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipRep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_dues_rep', models.BooleanField(blank=True, default=True, verbose_name='is dues rep?')),
                ('is_member_rep', models.BooleanField(blank=True, default=True, verbose_name='is member rep?')),
            ],
        ),
        migrations.CreateModel(
            name='CorporateMembershipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('position', models.IntegerField(default=0, null=True, verbose_name='Position', blank=True)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', verbose_name='Price')),
                ('renewal_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', null=True, verbose_name='Renewal Price')),
                ('admin_only', models.BooleanField(default=False, verbose_name='Admin Only')),
                ('apply_threshold', models.BooleanField(default=False, verbose_name='Allow Threshold')),
                ('individual_threshold', models.IntegerField(default=0, null=True, verbose_name='Threshold Limit', blank=True)),
                ('individual_threshold_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='All individual members applying under or equal to the threshold limit\nreceive the threshold prices. Additional employees can join but will be\ncharged the full individual corporate membership rate.\n', null=True, verbose_name='Threshold Price')),
                ('number_passes', models.PositiveIntegerField(default=0, verbose_name='Number Passes', blank=True)),
                ('creator', models.ForeignKey(related_name='corporate_memberships_corporatemembershiptype_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('entity', models.ForeignKey(related_name='corporate_memberships_corporatemembershiptype_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True)),
                ('membership_type', models.ForeignKey(help_text='Bind individual memberships to this membership type.', to='memberships.MembershipType', on_delete=django.db.models.deletion.CASCADE)),
                ('owner', models.ForeignKey(related_name='corporate_memberships_corporatemembershiptype_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorpProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('address', models.CharField(default='', max_length=150, verbose_name='Address', blank=True)),
                ('address2', models.CharField(default='', max_length=100, verbose_name='Address2', blank=True)),
                ('city', models.CharField(default='', max_length=50, verbose_name='City', blank=True)),
                ('state', models.CharField(default='', max_length=50, verbose_name='State', blank=True)),
                ('zip', models.CharField(default='', max_length=50, verbose_name='Zipcode', blank=True)),
                ('country', models.CharField(default='', max_length=50, verbose_name='Country', blank=True)),
                ('phone', models.CharField(default='', max_length=50, verbose_name='Phone', blank=True)),
                ('email', models.CharField(default='', max_length=200, verbose_name='Email', blank=True)),
                ('url', models.CharField(default='', max_length=100, verbose_name='URL', blank=True)),
                ('secret_code', models.CharField(default='', max_length=50, blank=True)),
                ('number_employees', models.IntegerField(default=0)),
                ('chapter', models.CharField(default='', max_length=150, verbose_name='Chapter', blank=True)),
                ('tax_exempt', models.BooleanField(default=False, verbose_name='Tax exempt')),
                ('annual_revenue', models.CharField(default='', max_length=75, verbose_name='Annual revenue', blank=True)),
                ('annual_ad_expenditure', models.CharField(default='', max_length=75, blank=True)),
                ('description', models.TextField(default='', blank=True)),
                ('expectations', models.TextField(default='', blank=True)),
                ('notes', models.TextField(default='', verbose_name='Notes', blank=True)),
                ('referral_source', models.CharField(default='', max_length=150, blank=True)),
                ('referral_source_other', models.CharField(default='', max_length=150, blank=True)),
                ('referral_source_member_name', models.CharField(default='', max_length=50, blank=True)),
                ('referral_source_member_number', models.CharField(default='', max_length=50, blank=True)),
                ('ud1', models.TextField(default='', null=True, blank=True)),
                ('ud2', models.TextField(default='', null=True, blank=True)),
                ('ud3', models.TextField(default='', null=True, blank=True)),
                ('ud4', models.TextField(default='', null=True, blank=True)),
                ('ud5', models.TextField(default='', null=True, blank=True)),
                ('ud6', models.TextField(default='', null=True, blank=True)),
                ('ud7', models.TextField(default='', null=True, blank=True)),
                ('ud8', models.TextField(default='', null=True, blank=True)),
                ('creator', models.ForeignKey(related_name='corporate_memberships_corpprofile_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('entity', models.ForeignKey(related_name='corporate_memberships_corpprofile_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True)),
                ('industry', models.ForeignKey(blank=True, to='industries.Industry', null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('owner', models.ForeignKey(related_name='corporate_memberships_corpprofile_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True)),
                ('region', models.ForeignKey(blank=True, to='regions.Region', null=True, on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Contact first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Contact last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Contact e-mail address')),
                ('hash', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FreePassesStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('corp_membership', models.ForeignKey(related_name='passes_used', to='corporate_memberships.CorpMembership', on_delete=django.db.models.deletion.CASCADE)),
                ('creator', models.ForeignKey(related_name='corporate_memberships_freepassesstat_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('entity', models.ForeignKey(related_name='corporate_memberships_freepassesstat_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True)),
                ('event', models.ForeignKey(related_name='passes_used', to='events.Event', on_delete=django.db.models.deletion.CASCADE)),
                ('owner', models.ForeignKey(related_name='corporate_memberships_freepassesstat_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True)),
                ('registrant', models.ForeignKey(to='events.Registrant', null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='IndivEmailVerification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50)),
                ('verified_email', models.CharField(max_length=200, verbose_name='email')),
                ('verified', models.BooleanField(default=False)),
                ('verified_dt', models.DateTimeField(null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('corp_profile', models.ForeignKey(to='corporate_memberships.CorpProfile', on_delete=django.db.models.deletion.CASCADE)),
                ('creator', models.ForeignKey(related_name='corp_email_veri8n_creator', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='corp_email_veri8n_updator', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndivMembershipRenewEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_detail', models.CharField(default='pending', max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')])),
                ('corp_membership', models.ForeignKey(to='corporate_memberships.CorpMembership', on_delete=django.db.models.deletion.CASCADE)),
                ('membership', models.ForeignKey(to='memberships.MembershipDefault', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('notice_name', models.CharField(max_length=250, verbose_name='Name')),
                ('num_days', models.IntegerField(default=0)),
                ('notice_time', models.CharField(max_length=20, verbose_name='Notice Time', choices=[('before', 'Before'), ('after', 'After'), ('attimeof', 'At Time Of')])),
                ('notice_type', models.CharField(max_length=20, verbose_name='For Notice Type', choices=[('approve_join', 'Approval Date'), ('disapprove_join', 'Disapproval Date'), ('approve_renewal', 'Renewal Approval Date'), ('disapprove_renewal', 'Renewal Disapproval Date'), ('expiration', 'Expiration Date')])),
                ('system_generated', models.BooleanField(default=False, verbose_name='System Generated')),
                ('subject', models.CharField(max_length=255)),
                ('content_type', models.CharField(default='html', max_length=10, verbose_name='Content Type', choices=[('html', 'HTML')])),
                ('sender', models.EmailField(max_length=255, null=True, blank=True)),
                ('sender_display', models.CharField(max_length=255, null=True, blank=True)),
                ('email_content', tendenci.libs.tinymce.models.HTMLField(verbose_name='Email Content')),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('creator_username', models.CharField(max_length=50, null=True)),
                ('owner_username', models.CharField(max_length=50, null=True)),
                ('status_detail', models.CharField(default='active', max_length=50, choices=[('active', 'Active'), ('admin_hold', 'Admin Hold')])),
                ('status', models.BooleanField(default=True)),
                ('corporate_membership_type', models.ForeignKey(blank=True, to='corporate_memberships.CorporateMembershipType', help_text="Note that if you don't select a corporate membership type, the notice will go out to all members.", null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('creator', models.ForeignKey(related_name='corporate_membership_notice_creator', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='corporate_membership_notice_owner', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('notice_sent_dt', models.DateTimeField(auto_now_add=True)),
                ('num_sent', models.IntegerField()),
                ('notice', models.ForeignKey(related_name='logs', to='corporate_memberships.Notice', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeLogRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('action_taken', models.BooleanField(default=False)),
                ('action_taken_dt', models.DateTimeField(null=True, blank=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('corp_membership', models.ForeignKey(related_name='log_records', to='corporate_memberships.CorpMembership', on_delete=django.db.models.deletion.CASCADE)),
                ('notice_log', models.ForeignKey(related_name='log_records', to='corporate_memberships.NoticeLog', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.AddField(
            model_name='corpmembershiprep',
            name='corp_profile',
            field=models.ForeignKey(related_name='reps', to='corporate_memberships.CorpProfile', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembershiprep',
            name='user',
            field=models.ForeignKey(verbose_name='Representative', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembershipauthdomain',
            name='corp_profile',
            field=models.ForeignKey(related_name='authorized_domains', to='corporate_memberships.CorpProfile', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='corp_memb_type',
            field=models.ManyToManyField(to='corporate_memberships.CorporateMembershipType', verbose_name='Corp. Memb. Type'),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='creator',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembershipapp_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='entity',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembershipapp_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='memb_app',
            field=models.OneToOneField(related_name='corp_app', default=1, on_delete=django.db.models.deletion.CASCADE, to='memberships.MembershipApp', help_text='App for individual memberships.', verbose_name='Membership Application'),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='owner',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembershipapp_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='corpmembershipapp',
            name='payment_methods',
            field=models.ManyToManyField(to='payments.PaymentMethod', verbose_name='Payment Methods'),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='anonymous_creator',
            field=models.ForeignKey(to='corporate_memberships.Creator', null=True, on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='approved_denied_user',
            field=models.ForeignKey(verbose_name='Approved or Denied User', to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='corp_profile',
            field=models.ForeignKey(related_name='corp_memberships', to='corporate_memberships.CorpProfile', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='corporate_membership_type',
            field=models.ForeignKey(verbose_name='MembershipType', to='corporate_memberships.CorporateMembershipType', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='creator',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembership_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='entity',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembership_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='invoice',
            field=models.ForeignKey(blank=True, to='invoices.Invoice', null=True, on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='owner',
            field=models.ForeignKey(related_name='corporate_memberships_corpmembership_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='corpmembership',
            name='payment_method',
            field=models.ForeignKey(default=None, verbose_name='Payment Method', to='payments.PaymentMethod', null=True, on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AlterUniqueTogether(
            name='corpmembershiprep',
            unique_together=set([('corp_profile', 'user')]),
        ),
    ]
