from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


categories = ['mexican','Gastropub','Whatever']
def validate_category(value):
    cap = value.capitalize()
    if not value in categories and not cap in categories:
        raise ValidationError(f'{value} is not a valid categories')
    