(function($){
    var session;
    function uuidv4() {
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
            (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16))
    }
    $(document).ready( function() {
        if(Cookies.get('gopanel') == undefined)
            Cookies.set('gopanel', uuidv4());
        $.ajaxSetup({cache:false});
        $.get('api/sites', {'session':Cookies.get('gopanel')}, function(data) {
            if(data.error != undefined)
                console.log(Cookies.get('gopanel'),data);
            else
                $.each(data, function(site,title) {
                    var item = $('#blank').clone().attr('id', site).insertAfter('#blank');
                    $(item).html(title).css('display', 'block');
                    $(item).click( function( e ) {
                        $.get('api/run', {'site':$(this).attr("id"),'session':Cookies.get('gopanel')}, function(rtn) {
                            if(rtn.go != undefined)
                                window.location = "/gopanel/"+rtn.go;
                            else console.log(Cookies.get('gopanel'), rtn);
                        });
                    });
                });
        })
        .fail(function() {
        });
        //$.get('api/info', {'site':'neocogent','session':Cookies.get('gopanel')}, function(data) {
        //    console.log('info:', data);
        //});
    });

})(jQuery);
