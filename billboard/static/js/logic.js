var Billboards = {};

Billboards.start = function() {
    $(document).ready(function() {
        Billboards.bindButtons();
    })
}

Billboards.bindButtons = function() {
    $("#add-post").click(Billboards.createNewPostField);
    $(".toggle-comments").click(Billboards.toggleComments);
    $(".submit-comment-btn").click(Billboards.submitComment);
}

Billboards.toggleComments = function(event) {
    event.preventDefault();
    var button = $(this);
    var postId = button.attr('id').split('-').pop();
    $(`#comment-container-${postId}`).toggleClass('invisible');
    var buttonText = button.text() === "Show" ? "Hide" : "Show";
    button.text(buttonText);
}

// Billboards.submitComment = function(event) {
//     event.preventDefault();
// }

Billboards.createNewPostField = function() {
    $("#new-post").css('display','block');
    $("#new-post legend").text(utils.getCurrentDateToDisplay());
    $("#new-post input[name='date_published']").attr('value',utils.getCurrentDateToSubmit());
    var plusButton = $("#add-post");
    plusButton.remove();
    var cancelButton = $("<button />").addClass('post-btn cancel-post-btn').append($("<i/>").addClass("fas fa-times"));
    var confirmButton = $("<button />").addClass('post-btn confirm-post-btn').attr('type','submit').attr('form','new-post-form')
    confirmButton.append($("<i/>").addClass('fas fa-check'));
    $(".add-post-container").append(cancelButton).append(confirmButton);
    cancelButton.click(Billboards.cancelNewPost);
}

Billboards.cancelNewPost = function() {
    var newPostSection = $("#new-post");
    newPostSection.css('display','none');
    var addPostContainer = $(".add-post-container");
    addPostContainer.empty();
    var plusButton = $("<button/>").attr('id',"add-post").addClass('add-post-btn post-btn').append($("<i/>").addClass('fas fa-plus'));
    addPostContainer.append(plusButton);
    plusButton.click(Billboards.createNewPostField);
}

Billboards.start();