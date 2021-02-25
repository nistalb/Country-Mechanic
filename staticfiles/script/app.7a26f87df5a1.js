
$(document).ready(function () {
    
    // Modals
    $("#signup_modal").click(function () {
        $(".signup").modal("show");
    });

    $(".signup").modal({
        closable: true
    });

    $(".signup").on('hide.bs.modal', function (e) {
        if (invalidForm) {
            e.preventDefault();
            $(".signup").modal("show");
        };
    });

    $("#login_modal").click(function() {
        $(".login").modal("show");
    });

    $(".login").modal({
        closable: true
    });

    $(".delete_modal_equipment").click(function () {
        $("#modal-"+this.id).modal("show");
    });

    $(".delete_equipment").modal({
        closable: true
    });

    $(".delete_modal_task").click(function () {
        $("#task_modal-"+this.id).modal("show");
    });

    $(".delete_task").modal({
        closable: true
    });

    $(".delete_modal_tool").click(function () {
        $("#tool_modal-"+this.id).modal("show");
    });

    $(".delete_tool").modal({
        closable: true
    });

    $(".delete_modal_consumable").click(function () {
        $("#consumable_modal-"+this.id).modal("show");
    });

    $(".delete_consumable").modal({
        closable: true
    });

    $(".delete_modal_profile").click(function () {
        $("#profile_modal").modal("show");
    });

    $(".delete_profile").modal({
        closable: true
    });

    $(".maint_modal_task").click(function () {
        $("#maintenance_modal").modal("show");
    });

    $(".task_maintenance").modal({
        closable: true
    });

    // video embedding on task show
    $('.ui.embed').embed();

    // Tabs on equipment show 
        // Title: jQuery folder tabs
        // Author: Axelaredz
        // Availability: https://codepen.io/axelaredz/pen/aswFo
    $("#tab_content div").hide(); 
    $("#tabs li:first").attr("id","current"); 
    $("#tab_content div:first").fadeIn(); 

    $('#tabs a').click(function(e) {
        e.preventDefault();
        if ($(this).closest("li").attr("id") == "current"){ 
            return       
        }
        else{             
            $("#tab_content div").hide(); 
            $("#tabs li").attr("id",""); 
            $(this).parent().attr("id","current"); 
            $('#' + $(this).attr('name')).fadeIn(); 
        }
    });
});
   