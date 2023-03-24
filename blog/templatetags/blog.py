from django import template

register = template.Library()


@register.simple_tag
def replace(request, key, value):
    url_dict = request.GET.copy()
    print(url_dict)
    print(url_dict.urlencode())
    
    url_dict[key] = value
    print(url_dict.urlencode())
    print()
    
    return url_dict.urlencode()