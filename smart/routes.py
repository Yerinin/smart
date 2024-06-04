def add_namespaces(api):
    from smart.app.main.main_controller import api as main_ns
    from smart.app.auth.controller.auth_controller import api as auth_ns

    api.add_namespace(main_ns, path="/")
    api.add_namespace(auth_ns, path="/")

