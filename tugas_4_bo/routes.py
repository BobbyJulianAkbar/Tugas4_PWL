def includeme(config):
    config.add_route("home", "/")
    config.add_route("login", "/login")
    config.add_route("register", "/logout")
    config.add_route("logout", "/register")
    config.add_route("buku", "/api/v1/buku")
    config.add_route("buku_create", "/api/v1/buku/create")
    config.add_route("buku_detail", "/api/v1/buku/{id}")
    config.add_route("buku_delete", "/api/v1/buku/delete/{id}")
    config.add_route("buku_update", "/api/v1/buku/update/{id}")
