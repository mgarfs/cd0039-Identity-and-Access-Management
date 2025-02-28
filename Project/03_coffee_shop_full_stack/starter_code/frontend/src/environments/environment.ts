export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'dev-mgarfs-fsnd.eu', // the auth0 domain prefix
    audience: 'coffeeshopapi', // the audience set for the auth0 app
    clientId: 'IPpJWeH40EP09vDovsGvV1uShurYmgJX', // the client id generated for the auth0 app
    callbackURL: 'https://127.0.0.1:8100', // the base url of the running ionic application. 
  }
};
