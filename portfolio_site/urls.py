from django.contrib import admin
from django.urls import path, include
##from quote_generator import views as quoteView
##from exchange_rate import views as exchangeView
# from blog import views as blogView
from portfolio import views as portfolioViews
from django.conf.urls.static import static
from django.conf import settings                                                        

urlpatterns = [
    path('admin/', admin.site.urls),
   ## path('exchange/', exchangeView.index, name="exchangeRate"),
    path('portfolio/', portfolioViews.home, name="portfolio"),
    # path('', quoteView.index, name='quoteGenerator'),
     path('', portfolioViews.home, name="home"),
    path('blog/', include('blog.urls')),
    # path('about/', views.about, name='about'),
    # path('blog/', include('blog.urls')),
        # path('blog/', blogView.all_blogs, name="blog"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
