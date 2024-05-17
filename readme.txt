celery -A metasnake worker --loglevel=info
celery -A metasnake worker --loglevel=info -P gevent  # for windows

celery -A metasnake beat --loglevel=info