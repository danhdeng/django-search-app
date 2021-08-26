from django.contrib.postgres import search
from django.shortcuts import render
from .forms import PostSearchForm
from .models import Book

# for SearchVector
from django.contrib.postgres.search import SearchVector

# import for Search Ranking
from django.contrib.postgres.search import SearchRank, SearchQuery

# import for TrigramSimilarity & TrigramDistance
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance

# import for SearhHeadline
from django.contrib.postgres.search import SearchHeadline

# Create your views here.


def post_search_view(request):
    form = PostSearchForm

    if "q" in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data["q"]
            # for case sensitive search
            # books = Book.objects.filter(title__contains=q)

            # for case insensitive searcch
            # books = Book.objects.filter(title__icontains=q)

            # full text search, must add "django.contrib.postgres" to INSTALLED_APPS section
            # books = Book.objects.filter(title__search=q)

            # SearchVerctor which will search again multiple field. here will perfomran serach
            # on both title and author fields
            # books = Book.objects.annotate(
            #     search=SearchVector("title", "authors")
            # ).filter(search=q)

            # Search Rank attempts to measure how relevant documents are to a particular query
            # vector = SearchVector("title", weight="A") + SearchVector(
            #     "authors", weight="B"
            # )
            # query = SearchQuery(q)
            # books = Book.objects.annotate(
            #     rank=SearchRank(vector, query, cover_density=True)
            # ).order_by("-rank")

            # Search with TrigramSimilarity & TrigramDistance
            # books = (
            #     Book.objects.annotate(
            #         similarity=TrigramSimilarity("title", q),
            #     )
            #     .filter(similarity__gte=0.3)
            #     .order_by("-similarity")
            # )
            # books = (
            #     Book.objects.annotate(
            #         similarity=TrigramSimilarity("title", q),
            #     )
            #     .filter(similarity__gte=0.23)
            #     .order_by("-similarity")
            # )
            books = (
                Book.objects.annotate(
                    distance=TrigramDistance("title", q),
                )
                .filter(distance__lte=0.8)
                .order_by("-distance")
            )

            # Search headline
            query = SearchQuery(q)
            vector = SearchVector("authors")
            books = Book.objects.annotate(
                search=vector,
                headline=SearchHeadline(
                    "authors", query, start_sel="<span>", stop_sel="<span>"
                ),
            ).filter(search=query)

            # to generate the query in the code
            # print(Book.objects.filter(title__icontains=q).query)

            # to get the analysis of the query like the sql execution plan
            print(Book.objects.filter(title__icontains=q).explain(analyze=True))

            return render(
                request, "index.html", {"form": form, "results": books, "q": q}
            )
