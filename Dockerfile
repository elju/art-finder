FROM ruby:2.3.0
MAINTAINER whitneymuseum whitney-api

ENV APP_HOME /vagrant/api

RUN apt-get update && apt-get install -qy mysql-client

RUN mkdir -p $APP_HOME /opt/whitney/lib
ADD ./Gemfile /opt/whitney/lib/
ADD ./Gemfile.lock /opt/whitney/lib/

WORKDIR /opt/whitney/lib
RUN bundle install

WORKDIR $APP_HOME
EXPOSE 4000
CMD /bin/bash -c "rm tmp/pids/server.pid; bundle exec rake db:create db:migrate; rails s -p 4000 -b '0.0.0.0'"
