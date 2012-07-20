#snout

## django url generation via inspection

## what
use `snout` to generate routes for your django apps using inspection, so you can do more interesting things.

instead of this:

    # breakfast/urls.py
    urlpatterns =  patterns('',
        url(r'^$','breakfast.views.index'),
        url(r'^order/$''', 'breakfast.views.order'),
        url(r'^waffles/$''', 'breakfast.views.waffles'),
        url(r'^sausage/$''', 'breakfast.views.sausage'),
    )
 

django apps can do this:

    # breakfast/urls.py
    urlpatterns = snout.make_django_patterns(breakfast)

awww yeah


## how

 `ham_and_eggs` will be assigned to the route `ham-and-eggs`

this way, when you want to add more items to your breakfast web app, you can just add the `ham_and_eggs` function
