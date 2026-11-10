import json
import socket
from datetime import datetime, timezone

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# In-memory storage (resets on restart) - no database
ITEMS = [{"id": 1, "name": "Learn Django"}, {"id": 2, "name": "Deploy React with PM2"}]


def health(request):
    return JsonResponse({"status": "ok"})


def message(request):
    return JsonResponse({
        "message": "Hello from Django backend!",
        "hostname": socket.gethostname(),
        "time": datetime.now(timezone.utc).isoformat(),
    })


@csrf_exempt
def items(request):
    if request.method == "POST":
        try:
            name = json.loads(request.body or "{}").get("name", "").strip()
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid JSON"}, status=400)
        if not name:
            return JsonResponse({"error": "name is required"}, status=400)
        item = {"id": max([i["id"] for i in ITEMS], default=0) + 1, "name": name}
        ITEMS.append(item)
        return JsonResponse(item, status=201)
    return JsonResponse({"items": ITEMS})
