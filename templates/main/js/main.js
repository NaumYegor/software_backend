(function () {
    function initialize() {
        var mapOptions = {
            zoom: 14,
            center: new google.maps.LatLng(23.7893837, 90.38596079999999),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map'), mapOptions);

        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(23.7893837, 90.38596079999999),
        });

        marker.setMap(map);
        var infowindow = new google.maps.InfoWindow({
            content: "Hello World!"
        });

        infowindow.open(map, marker);

        //add overlay
        map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(document.getElementById('map-overlay'));
    }

    google.maps.event.addDomListener(window, 'load', initialize);
   // navigator.geolocation.getCurrentPosition(initialize);
    jQuery(document).ready(function ($) {


        $(".embed-responsive iframe").addClass("embed-responsive-item");
        $(".carousel-inner .item:first-child").addClass("active");

        $('[data-toggle="tooltip"]').tooltip();

        $('.gallery-btn a').click(function () {

            $(".gallery-btn a").removeClass("active");
            $(this).addClass("active");

            var selector = $(this).attr('data-filter');
            $(".gellery-item").isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });
       // jQeury smooth scroll
        $("li.smooth-scroll a").bind("click", function(event){
            var $anchor = $(this);
            var headerH = "50";
            $("html, body")
                .stop()
                .animate({
                scrollTop: $($anchor.attr("href"))
                    .offset()
                    .top - headerH + "px"
            }, 1200, "easeOutCirc");

            event.preventDefault();

        });
        //jquery scroll spy
        $("body").scrollspy({
            target: ".navbar-collapse",
            offset: 95
        });
        new WOW().init();
        //Pretty Photo
        $("a[data-gallery^='prettyPhoto']").prettyPhoto({
            social_tools: false
        });


		var instaPhotoHTML = ['<div class="single-gl web ', ' col-md-2 col-sm-3"><img src="', '" alt=""><a href="', '"><div class="gl-overlay"></div></a></div>']

		$.ajax({
			type: 'GET',
			async: true,
			url: '/insta/recent',
			success: function(data) {
				//alert(data);
				var photosContainer = jQuery('.gellery-item.text-center'),
					changeInsts = {
						'student.nure': 'student_nure',
						'i_nure': 'i_nure',
						'senat.nure.ua': 'senat_nure_ua'
					},
					photoHTML;
				for (let inst in data) {
					//alert(inst);
					for (let photo in data[inst]) {
						photoHTML = instaPhotoHTML[0] + changeInsts[inst] + instaPhotoHTML[1] + data[inst][photo] + instaPhotoHTML[2] + photo + instaPhotoHTML[3];
						//alert(photoHTML);
						photosContainer.append(photoHTML);
					}
				}
			},
			error: function() {
				alert('Error...');
			}
		})
    });


    jQuery(window).load(function () {


    });



}(jQuery));