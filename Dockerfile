FROM python:2.7
MAINTAINER coopandluke watartu

ENV APP_HOME /watartu

RUN apt-get update
WORKDIR $APP_HOME
ADD install.sh ./install.sh
ADD opencv-2.4.11.zip ./opencv-2.4.11.zip
RUN ./install.sh

# RUN mkdir -p $APP_HOME /opt/whitney/lib
# ADD ./Gemfile /opt/whitney/lib/
# ADD ./Gemfile.lock /opt/whitney/lib/
# 
# WORKDIR /opt/whitney/lib
# RUN bundle install
# 
# WORKDIR $APP_HOME
# EXPOSE 4000
CMD echo "hi"
