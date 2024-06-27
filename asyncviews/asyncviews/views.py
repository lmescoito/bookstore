import asyncio
from django.http import HttpResponse

async def simple_async_view(request):
    try:
        await asyncio.sleep(1)
        return HttpResponse("Simple async view working")
    except Exception as e:
        print(f"Error in simple_async_view: {e}")
        return HttpResponse("Internal Server Error", status=500)
