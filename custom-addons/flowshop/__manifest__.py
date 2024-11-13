{
    "name": "Flowshop",
    "author": "Flowshop",
    "website": "www.flowshop.tech",
    "summary": "It's Flowshop",
    "depends": ["mail", "base_automation"],
    "data": [
        "security/role.xml",
        "security/rule.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu.xml",
        "views/table.xml",
    ],
    "application": True,
    "assets": {
        "web.assets_backend": [
            "flowshop/static/src/css/**",
            "flowshop/static/src/js/**",
        ],
    },
}
