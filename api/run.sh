kill `cat gunicorn.pid`
GUNICORN_CMD_ARGS="-w 3 -b 127.0.0.1:8001 -p gunicorn.pid --capture-output True --log-file gunicorn.log" gunicorn api.wsgi &
