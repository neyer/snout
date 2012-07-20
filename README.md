#snout

## django url pattern generation via inspection

## what
use `snout` to generate routes for your django apps using inspection, so you can do more interesting things.

instead of this:

    # breakfast/urls.py
    from django.conf.urls import patterns, url
    urlpatterns =  patterns('',
        url(r'^$','breakfast.views.index'),
        url(r'^order/$''', 'breakfast.views.order'),
        url(r'^waffles/$''', 'breakfast.views.waffles'),
        url(r'^sausage/$''', 'breakfast.views.sausage'),
        url(r'^toast/(?P<num_slices>\d+)$''', 'breakfast.views.toast'),
    )
 

now you can do this:

    # breakfast/urls.py
    import views
    import snout
    urlpatterns = snout.make_django_patterns(views)

awww yeah

## how

`make_django_patterns` creates a route for all functions in the given module, except those starting with "_"

 underscores (_) are replaced with dashes (-) because why not?

 a view named "index" is given the route "^$" by default

 any arguments to your view (other than "requests") are assigned regular expression match groups. 


## why

laziness
