from urlparse import urljoin

# Set LOCAL_STORE to True if you want brwsr to just load a (smallish) RDF file into server memory
# rather than operate on an external SPARQL store
LOCAL_STORE = False

# Set LOCAL_FILE to the relative or absolute path of the file you want brwsr to load when
# LOCAL_STORE is True. The brwsr application will just use RDFLib to guess the file format based on the extension.
# You can use UNIX file masks such as * and ? to load multiple files
LOCAL_FILE = 'justsomeexample.trig'

# Set this to the SPARQL endpoint uri of your triplestore
# e.g. "http://dbpedia.org/sparql"
SPARQL_ENDPOINT = "http://your.sparql.endpoint.here/sparql"

# If brwsr is backed by multiple separate triple stores, use SPARQL_ENDPOINT_MAPPING to
# make sure that each URI for which the LOCAL_NAME (i.e. the URI with the DEFAULT_BASE removed)
# starts with a key of the SPARQL_ENDPOINT_MAPPING file, the proper SPARQL endpoint is used.
# Example:
# SPARQL_ENDPOINT_MAPPING = {
#     "/example": "http://the.sparql.endpoint.for.uris.starting.with/example/sparql"
# }
SPARQL_ENDPOINT_MAPPING = {}

# The DEFAULT_BASE is the prefix of the URI's in the triple store that can be browsed by brwsr
# Requests to brwsr only include the local name (i.e. the the part after the third slash '/'),
# the DEFAULT_BASE is *always* prepended to this local name to make up the URI that's used to
# query the triple store
# e.g. "http://dbpedia.org" (without the last slash!)
DEFAULT_BASE = "http://your.base.uri.here"

# The LOCAL_DOCUMENT_INFIX is the infix used between the DEFAULT_BASE and the local name of the URI
# to denote the HTML representation of the RDF resource (see the Cool URI's specification)
LOCAL_DOCUMENT_INFIX = 'doc'

# The LOCAL_SERVER_NAME is the address brwsr listens to. It needs to know this to build proper
# requests when you click a URI in the brwsr page of a resource.
# e.g. "http://localhost:5000" if running flask.
LOCAL_SERVER_NAME = "http://your.server.name.here"

# By default brwsr assumes it is running at the root of the server,
# If you want to run brwsr under a directory (e.g. http://example.com/brwsr rather than http://example.com), you need to do this
# via a reverse proxy, and tell brwsr about it (set BEHIND_PROXY to True)
#
#########
# Example Nginx configuration (adapted from http://flask.pocoo.org/snippets/35/)
#########
#
# location /myprefix {
#        proxy_pass http://localhost:5000;
#        proxy_set_header Host $host;
#        proxy_set_header Upgrade $http_upgrade;
#        proxy_set_header Connection "upgrade";
#        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#        proxy_set_header X-Scheme $scheme;
#        proxy_set_header X-Script-Name /myprefix;
#        }
#
# Where 'myprefix' should be set to the location you want to be running brwsr under
# The 'proxy_pass' setting should point to the address and port you are running brwsr at (default is localhost port 5000).
#
#########
BEHIND_PROXY = False


# The START_LOCAL_NAME is the local name of the first URI shown in brwsr if no URI is specified
# e.g. "resource/Amsterdam" when using the DBPedia settings
START_LOCAL_NAME = "some/local/name"

# The START_URI is simply the combination of the DEFAULT_BASE and the START_LOCAL_NAME
# (i.e. there is no need to change this, usually)
# e.g. this will become "http://dbpedia.org/resource/Amsterdam"
START_URI = urljoin(DEFAULT_BASE,START_LOCAL_NAME)

# Set query results limit because otherwise your browser might crash.
QUERY_RESULTS_LIMIT = 1000

# The port via which to run brwsr
PORT = 5000

# Debug logging
DEBUG = False

# Browse URIs that do not match the DEFAULT_BASE
BROWSE_EXTERNAL_URIS = True

# Dereference external URIs (i.e. retrieve RDF served at that location, and display the resource)
# NB: This may be slow, depending on the responsiveness of the server at hand
# NB: The resulting RDF is stored locally (in memory) which means that this is a potential memory hog for
# servers that are visited frequently. TODO: store results in a triple store
DEREFERENCE_EXTERNAL_URIS = False

# Set any custom parameters to be sent to the SPARQL endpoint
# e.g. CUSTOM_PARAMETERS = {'reasoning': 'true'} for Stardog
CUSTOM_PARAMETERS = {'reasoning': 'true'}
