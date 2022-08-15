from allauth.account.forms import LoginForm


class bootstrap_login(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['remember'].label = 'Remember me: '
        self.fields['remember'].initial = True
        for visible in self.visible_fields():
            if visible.name != 'remember':
                visible.field.widget.attrs['class'] = 'form-control'

