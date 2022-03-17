
jinja2 ts-generic.json.j2 -o ts-service.json -D client=false
jinja2 ts-generic.json.j2 -o ts-tool.json -D client=false
jinja2 ts-generic.json.j2 -o ts-client.json -D client=true
jinja2 ts-generic.json.j2 -o ts-lib-service.json -D client=false -D lib=true
jinja2 ts-generic.json.j2 -o ts-lib-client.json -D client=true -D lib=true
jinja2 ts-generic.json.j2 -o ts-lib-client-public.json -D public=true -D client=true -D lib=true
