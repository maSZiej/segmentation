server{
    listen ${LISTEN_PORT}

    location /static{
        alias/vol/static/;
    }

    location /static{
        alias /vol/media/;
    }


    location / {
        proxy_pass http://${APP_HOST}:${APP_PORT}
        inculde /etc/nginx/proxy_params
    }
}