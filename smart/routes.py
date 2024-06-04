def add_namespaces(api):
    from smart.controllers.main_controller import api as main_ns

    api.add_namespace(main_ns, path="/")

