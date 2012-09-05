from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five import BrowserView
from zope.interface import implements
from collective.listingviews.interfaces import IListingViews
from collective.listingviews.settings import ListingSettings
from collective.listingviews.adapters import BasicAdapter


class ListingView(BrowserView):
    """
    View for file will redirect to download if user can't edit it.
    """
    implements(IListingViews)
    select_listing_view = ViewPageTemplateFile("templates/layout.pt")

    def __init__(self, context, request):
        super(ListingView, self).__init__(context, request)
        self.adapter = BasicAdapter(self.context, self.request)
        self.settings = ListingSettings(self.context, interfaces=[self.adapter.schema])
