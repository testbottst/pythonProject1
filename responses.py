from datetime import datetime

def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("הזמנה", "אזמנה", "הזמנהה",):

        return "להזמנה יש ללחוץ על הקישור הבא: @WeDoWeDoo"

    if userMessage in ("תפריט",):
        return "https://t.me/weedoooooo/7"

    if userMessage in ("time", "time?","what is the time?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(dateTime)


    return "יש לכתוב ״הזמנה״ או ״תפריט״ ולשלוח את ההודעה"
