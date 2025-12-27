list:
    just --list

make arg1="":
    uv run make html {{arg1}}

slug:
    md-slug

test arg1="":
    uv run -m pytest {{arg1}}
