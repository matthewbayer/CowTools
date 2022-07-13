def generate_context(request, extra=None):
    logged_in = request.user.is_authenticated
    context = {**context, **extra} if extra else {"logged_in": logged_in}
    return context
