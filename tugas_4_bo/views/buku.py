from pyramid.view import view_config
from .. import models
from sqlalchemy.exc import SQLAlchemyError
import json
import traceback


@view_config(route_name="buku", renderer="json", request_method="GET")
def get_buku(request):
    try:
        results = request.dbsession.query(models.Buku).all()
        return {
            "status": "success",
            "data": [
                dict(
                    id=row.id,
                    title=row.title,
                    description=row.description,
                    year=row.year,
                )
                for row in results
            ],
        }
    except SQLAlchemyError as e:
        request.response.status = 500
        return {"status": "error", "message": str(e.orig)}
    except Exception as e:
        print(traceback.format_exc())
        request.response.status = 500
        return {"status": "error", "message": str(e)}


@view_config(route_name="buku_detail", renderer="json", request_method="GET")
def get_buku_detail(request):
    try:
        query = request.dbsession.query(models.Buku)
        result = query.filter(models.Buku.id == request.matchdict["id"]).first()

        if result is None:
            request.response.status = 404
            return {"status": "error", "message": "Not Found"}

        return {
            "status": "success",
            "data": {
                "id": result.id,
                "title": result.title,
                "description": result.description,
                "year": result.year,
            },
        }
    except SQLAlchemyError as e:
        request.response.status = 500
        return {"status": "error", "message": str(e.orig)}


@view_config(
    route_name="buku_create",
    renderer="json",
    request_method="POST",
    permission="admin",
)
def create_buku(request):
    try:
        buku = models.Buku(
            title=request.json_body["title"],
            year=request.json_body["year"],
            description=request.json_body["description"],
        )
        request.dbsession.add(buku)
        return {"status": "success", "data": request.json_body}
    except SQLAlchemyError as e:
        request.response.status = 500
        return {"status": "error", "message": str(e.orig)}
    except KeyError as e:
        request.response.status = 500
        return {"status": "error", "message": str(e) + " not found"}
    except Exception as e:
        request.response.status = 500
        return {"status": "error", "message": str(e)}


@view_config(
    route_name="buku_update", renderer="json", request_method="PUT", permission="admin"
)
def update_buku(request):
    try:
        query = request.dbsession.query(models.Buku)
        buku = query.filter(models.Buku.id == request.matchdict["id"]).first()

        if buku is None:
            request.response.status = 404
            return {"status": "error", "message": "Not Found"}

        buku.title = request.json_body["title"]
        buku.description = request.json_body["description"]
        buku.year = request.json_body["year"]
        return {"status": "success", "data": request.json_body}
    except SQLAlchemyError as e:
        return {"status": "error", "message": str(e.orig)}
    except KeyError as e:
        return {"status": "error", "message": str(e) + " not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@view_config(
    route_name="buku_delete",
    renderer="json",
    request_method="DELETE",
    permission="admin",
)
def delete_buku(request):
    try:
        query = request.dbsession.query(models.Buku)
        buku = query.filter(models.Buku.id == request.matchdict["id"]).first()

        if buku is None:
            request.response.status = 404
            return {"status": "error", "message": "Not Found"}

        request.dbsession.delete(buku)
        return {"status": "success"}
    except SQLAlchemyError as e:
        return {"status": "error", "message": str(e.orig)}
    except KeyError as e:
        return {"status": "error", "message": str(e) + " not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
