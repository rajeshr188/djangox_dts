from tenant_schemas.middleware import BaseTenantMiddleware
from tenant_schemas.utils import get_public_schema_name

class RequestUserTenantMiddleware(BaseTenantMiddleware):
    
    def get_tenant(self,model,hostname,request):
        try:
            ps = model.objects.get(schema_name=get_public_schema_name())
        except model.DoesNotExist:
            print("create public schema first")

            ps='public'
        try:
            if not request.user.is_anonymous and request.user.company:
                tenant_model = request.user.company
            else:
                tenant_model = ps
            print(tenant_model,ps)
            return tenant_model
        except model.DoesNotExist:
            print("create user schema first")
            return ps     
