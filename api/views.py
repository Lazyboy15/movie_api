from .models import Movie
from .serializers import MovieSerializer# Create your views here.
class IndexView(APIView):
    """
    API view for searching Movies
    """
    allowed_methods = ['GET']
    serializer_class = MovieSerializer

def get(self, request, *args, **kwargs):
    queryset = Movie.objects.all()
    # We can filter our movies by name
	name = request.query_params.get('name', None)

	if name is not None:
		queryset = queryset.filter(name__icontains=name)        
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)