from config import settings
from config.celery import app
from datetime import datetime, timedelta, timezone, date
from djangocourse.models import DistributionList
from django.core.mail import send_mail
import pytz

@app.task
def repeat_order_make():
    for row in DistributionList.objects.all():
        mailing_time = row.time.replace(second=0, microsecond=0)
        mailing_date = row.date
        time_now = datetime.now().time().replace(second=0, microsecond=0)
        date_now = date.today()
        if mailing_time == time_now and row.status == DistributionList.STATUS_LAUNCHED and mailing_date == date_now:
            try:
                send_mail(
                    subject=row.message.theme,
                    message=row.message.text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[row.client.email],
                    fail_silently=False
                )
                #Формирование отчета если отправлено успешно
            except:
                pass
                #Формирование отчета если не отправлено

            if row.periodicity == DistributionList.PERIOD_DAY:
                mailing_date += timedelta(days=1)
                DistributionList.objects.update(date=mailing_date)
            elif row.periodicity == DistributionList.PERIOD_WEEK:
                mailing_date += timedelta(days=7)
                DistributionList.objects.update(date=mailing_date)
            elif row.periodicity == DistributionList.PERIOD_MONTH:
                mailing_date += timedelta(days=30)
                DistributionList.objects.update(date=mailing_date)
        else:
            print(f'Ему не отправляю {row.client.last_name}, {row.time}, {row.message.theme}, {row.status},{row.client.email}, {row.date}')
            print(time_now, date_now)


