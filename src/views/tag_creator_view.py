from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''
    def validate_and_create(self, htpp_request: HttpRequest) -> HttpResponse:
        body = htpp_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        print("Criando tag para o produto", product_code)
        # retorno HTTP
        return HttpResponse(200, body={"hello": "world"})
    