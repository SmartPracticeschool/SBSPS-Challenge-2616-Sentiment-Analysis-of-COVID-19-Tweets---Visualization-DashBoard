var express = require('express');
var router = express.Router();

var wml_credentials = {
    "apikey": "qf_53KWilRo8Na0B20F4FtIVmzSNmFqw5b1F48dL-Yve",
    "instance_id": "2916f100-7805-4080-8431-fdb70c143b1e"
};

var apikey = "3VPOLe-LV9vmCxGOIn50ndgyhVrHHgwnT63xpWHDSKAE";
var endpoint_url = "https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/01feab98-fb22-4546-bed3-5277497bcf5f/deployments/f0de912c-db60-4302-b24e-458eb859726e/online";

var instance_id = "01feab98-fb22-4546-bed3-5277497bcf5f";

var payload = {

	"values" : [ [ 10, 10 ] ] ,
};



function processdata( endpoint_url, payload )
{
    return new Promise( function( resolve, reject )
    {
        if( "" == endpoint_url )
        {
            reject( "Endpoint URL not set in 'server.js'" );
        }
        else
        {
            getAuthToken( wml_credentials["apikey"] ).then( function( iam_token )
            {
                sendtodeployment( endpoint_url, iam_token, wml_credentials["instance_id"], payload ).then( function( result )
                {
                    resolve( result );

                } ).catch( function( processing_error )
                {
                    reject( "Send to deployment error: " + processing_error );

                } );

            } ).catch( function( token_error )
            {
                reject( "Generate token: " + token_error );

            } );
        }

    } );    

}


function getAuthToken( apikey )
{
    // Use the IBM Cloud REST API to get an access token
    //
    var IBM_Cloud_IAM_uid = "bx";
    var IBM_Cloud_IAM_pwd = "bx";
    
    return new Promise( function( resolve, reject )
    {
        var btoa = require( "btoa" );
        var options = { url     : "https://iam.bluemix.net/oidc/token",
                        headers : { "Content-Type"  : "application/x-www-form-urlencoded",
                                    "Authorization" : "Basic " + btoa( IBM_Cloud_IAM_uid + ":" + IBM_Cloud_IAM_pwd ) },
                        body    : "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey" };

        var request = require( 'request' );
        request.post( options, function( error, response, body )
        {
            if( error || ( 200 != response.statusCode ) )
            {
                console.log( "getAuthToken:\n" + JSON.parse( body )["errorCode"] + "\n" + JSON.parse( body )["errorMessage"] + "\n" + JSON.parse( body )["errorDetails"] )
                reject( "Status code: " + response.statusCode + "  Error: " + error );
            }
            else
            {
                try
                {
                    resolve( JSON.parse( body )["access_token"] );
                    console.log(body);
                }
                catch( e )
                {
                    reject( 'JSON.parse failed.' );
                }
            }

        } );

    } );    

}



async function sendtodeployment( endpoint_url, apikey, instance_id, payload )
{
    // Use the IBM Watson Machine Learning REST API to send the payload to the deployment
    // https://watson-ml-api.mybluemix.net/
    //
    var iam_token = await getAuthToken(apikey);


    return new Promise( function( resolve, reject )
    {
        var options = { url     : endpoint_url,
                        headers : { "Content-type"   : "application/json",
                                    "Authorization"  : "Bearer " + iam_token,
                                    "ML-Instance-ID" : instance_id },
                        body    : JSON.stringify( payload ) };

        var request = require( 'request' );
        request.post( options, function( error, response, body )
        {
            if( error )
            {
                reject( error );
            }
            else
            {
                try
                {
                    resolve( JSON.parse( body ) );
                    console.log(body);
                }
                catch( e )
                {
                    reject( 'JSON.parse failed.' );
                }
            }

        } );

    } );

}


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.post('/form-submit', async function(req, res, next) {


  var dateString= req.body["Date"] ; //input string that u have to put means payload

var year= dateString.slice(0,4);
var month = dateString.slice(5,7);
var day = dateString.slice(8,10);
var s4 = "/";
var ans = month.concat(s4,day,s4,year);
var date1 = new Date("03/14/2020"); 
var date2 = new Date(ans); 
var Difference_In_Time = date2.getTime() - date1.getTime();  

	var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24); 
	 
	 var state = req.body["State"]


	// // document.write(Difference_In_Days); 

	var payload = {
	"values" : [ [ Difference_In_Days , state ] ] ,
	};

	console.log(payload);
  
  
//   const secondFunction = async () => {
//   const result = await firstFunction()
//   // do something else here after firstFunction completes
// }


 // console.log(req.body);
  var response = await sendtodeployment(endpoint_url, apikey, instance_id,  payload)

  // console.log("logging response" + response)
  res.render('form-submit', { query: response });

});


module.exports = router;
