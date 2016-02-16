Webcam.set({
	width: 320,
	height: 240,
	dest_width: 640,
	dest_height: 480,
	image_format: 'jpeg',
	jpeg_quality: 90
});
Webcam.attach('#my_camera');

function take_snapshot() {
    // take snapshot and get image data
    Webcam.snap( function(data_uri) {
    // display results in page
        document.getElementById('results').innerHTML = 
            '<h2>Here is your large image:</h2>' + 
            '<img src="'+data_uri+'"/>';
        Webcam.upload( data_uri, 'submit/', function(code, text) {
            debugger;
            document.getElementById('results').innerHTML =
              '<h2>Here\'s what you matched</h2>'+
              '<img src="/images'+text.slice(1,text.length)+'"></img>';
        });
    } );
}
