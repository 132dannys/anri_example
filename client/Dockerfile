FROM node:19

WORKDIR /client

ENV PATH /NewManagementApp/client/node_modules/.bin:$PATH

COPY package.json /client
RUN npm install

COPY . /client

CMD npm run serve