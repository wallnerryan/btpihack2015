FROM hypriot/rpi-alpine-scratch

RUN apk update &&\
apk upgrade &&\
apk add bash &&\
apk add netcat-openbsd &&\
rm -rf /var/cache/apk/*

EXPOSE 4444

#CMD nc -l 4444 > received_data
CMD bash
