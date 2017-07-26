
Survey.Survey.cssType = "bootstrap";
Survey.defaultBootstrapCss.navigationButton = "btn btn-green";

Survey.JsonObject.metaData.addProperty("dropdown", {name: "renderAs", default: "standard", choices: ["standard", "imagepicker"]});

window.survey = new Survey.Model({ questions: [
 { type: "dropdown", name: "luggage", renderAs: "imagepicker", title: "You have 5 minutes... grab your luggage!",
     choices: [
        {value: "backpack", text: "../resources/backpack.png"},
        {value: "briefcase", text: "../resources/briefcase.png"},
        {value: "purse", text: "../resources/purse.png"},
        {value: "luggage", text: "../resources/luggage.png"},
        {value: "plastic-bag", text: "../resources/plastic-bag.png"}
     ]
  },  { type: "dropdown", name: "partner", renderAs: "imagepicker", title: "Who are you traveling with?",
       choices: [
          {value: "best friend", text: "../resources/best_friend.png"},
          {value: "family", text: "../resources/family.png"},
          {value: "solo", text: "../resources/solo.png"},
          {value: "wife", text: "../resources/wife.png"}
       ]
    }, { type: "dropdown", name: "stay", renderAs: "imagepicker", title: "ZzzzZZ... Time to rest! Select a place to stay: ",
        choices: [
           {value: "airbnb", text: "../resources/airbnb.png"},
           {value: "resort", text: "../resources/hilton.png"},
           {value: "tent", text: "../resources/tent.png"},
           {value: "luxury", text: "../resources/luxuryresort.png"}
        ]
     }, { type: "dropdown", name: "budget", renderAs: "imagepicker", title: "What is your budget?",
         choices: [
            {value: "little", text: "../resources/money-bag.png"},
            {value: "normal", text: "../resources/moneybag.png"},
            {value: "a lot", text: "../resources/moneybag2.png"},
         ]
      }, { type: "dropdown", name: "bucketList", renderAs: "imagepicker", title: "The first thing on my bucket list is: ",
          choices: [
             {value: "outdoors", text: "../resources/boat.png"},
             {value: "foodie", text: "../resources/cutlery.png"},
             {value: "shopping", text: "../resources/mall.png"},
             {value: "touristy", text: "../resources/maya.png"},
             {value: "beach", text: "../resources/surf.png"}
          ]
       },{ type: "dropdown", name: "essential", renderAs: "imagepicker", title: "My number one travel essential is: ",
           choices: [
              {value: "phone", text: "../resources/phone.png"},
              {value: "coffee", text: "../resources/mug.png"},
              {value: "camera", text: "../resources/camera.png"},
              {value: "hiking shoes", text: "../resources/hiking.png"},
              {value: "drink", text: "../resources/wine-bottle.png"}
           ]
        }, { type: "dropdown", name: "message", renderAs: "imagepicker", title: "You send a message to a friend during your vacation. What would you say?",
           choices: [
              {value: "wilderness", text: "../resources/wilderness.png"},
              {value: "tanline", text: "../resources/tanline.png"},
              {value: "restaurant", text: "../resources/rest.png"},
              {value: "museums", text: "../resources/museums.png"},
           ]
        }, { type: "dropdown", name: "food", renderAs: "imagepicker", title: "Food is served! Grab your plate",
           choices: [
              {value: "sushi", text: "../resources/sushi.png"},
              {value: "pizza", text: "../resources/pizza.png"},
              {value: "steak", text: "../resources/steak.png"},
              {value: "salad", text: "../resources/salad.png"},
           ]
        }, { type: "dropdown", name: "souvenir", renderAs: "imagepicker", title: "A souvenir shop! What are you buying?",
           choices: [
              {value: "diamond", text: "../resources/diamond.png"},
              {value: "rose", text: "../resources/rose.png"},
              {value: "totem", text: "../resources/totem.png"},
              {value: "surfing", text: "../resources/surf.png"},
           ]
        }
]});
survey.onComplete.add(function(result) {
  if(result.data["luggage"]=="purse" //|| result.data["luggage"]=="luggage"
      && result.data["stay"]=="luxury"
      && result.data["budget"]=="a lot"
      && result.data["bucketList"]!="outdoors" && result.data["bucketList"]!="beach"
      && result.data["essential"]=="phone" || result.data["essential"]=="coffee"
      && result.data["message"]=="restaurant" || result.data["message"]=="tanline"
      && result.data["food"]=="sushi" || result.data["food"]=="steak"
      && result.data["souvenir"]=="diamond" || result.data["souvenir"]=="rose"){
    window.location.replace('/maldives');

  }else if(result.data["luggage"]=="purse" || result.data["luggage"]=="luggage"
      && result.data["stay"]=="luxury"
      && result.data["budget"]=="a lot"
      && result.data["bucketList"]!="outdoors" && result.data["bucketList"]!="beach"
      && result.data["essential"]=="phone" || result.data["essential"]=="coffee"
      && result.data["message"]=="restaurant" || result.data["message"]=="tanline"
      && result.data["food"]=="sushi" || result.data["food"]=="steak"
      && result.data["souvenir"]=="diamond" || result.data["souvenir"]=="rose"){
    window.location.replace('/santorini');

  }else if(result.data["luggage"]=="purse" || result.data["luggage"]=="luggage"
      && result.data["stay"]=="luxury"
      && result.data["partner"]!="family"
      && result.data["budget"]=="a lot"
      && result.data["bucketList"]!="touristy"
      && result.data["essential"]=="phone" || result.data["essential"]=="camera" || result.data["essential"]=="drink"
      && result.data["message"]=="restaurant" || result.data["message"]=="tanline"
      && result.data["food"]=="steak" || result.data["food"]=="salad"
      && result.data["souvenir"]!="totem"){
    window.location.replace('/santorini');

  }else if(result.data["luggage"]=="briefcase" || result.data["luggage"]=="purse" ||result.data["luggage"]=="luggage"
      && result.data["stay"]=="airbnb" || result.data["stay"]=="resort" || result.data["stay"]=="luxury"
      && result.data["budget"]!="little"
      && result.data["bucketList"]!="shopping"
      && result.data["essential"]=="camera" || result.data["essential"]=="drink" || result.data["essential"]=="phone"
      && result.data["message"]=="restaurant" || result.data["message"]=="tanline" || result.data["message"]=="tanline"
      && result.data["food"]=="sushi" || result.data["food"]=="salad"
      && result.data["souvenir"]=="diamond" || result.data["souvenir"]=="rose"){
    window.location.replace('/hongkong');

  }else if(result.data["luggage"]=="briefcase" || result.data["luggage"]=="purse" ||result.data["luggage"]=="luggage"
      && result.data["stay"]=="airbnb" || result.data["stay"]=="resort" || result.data["stay"]=="luxury"
      && result.data["budget"]!="little"
      && result.data["essential"]!="hiking shoes"
      && result.data["message"]!="wilderness"){
    window.location.replace('/dubai');

  }else if(result.data["luggage"] == "backpack"
  && result.data["food"] != "sushi"
  && result.data["souvenir"] == "rose"
  && result.data["budget"] == "normal"
  && result.data["stay"] == "tent"
  ){window.location.replace('/newzealand');

  }else if(result.data["luggage"] == "backpack"
  && result.data["souvenir"] == "rose"
  && result.data["budget"] == "normal"
  && result.data["stay"] == "tent"
  ){window.location.replace('/canada');

  }else if(result.data["luggage"] != "briefcase"
  && result.data["food"] != "sushi"
  && result.data["souvenir"] == "rose"
  && result.data["budget"] == "little"
  && result.data["bucketlist"] == "touristy"
  && result.data["stay"] == "airbnb"
  ){window.location.replace('/mexicocity');

  } else if(
    result.data["luggage"] != "briefcase"
    && result.data["souvenir"] == "totem"
    && result.data["budget"] == "little"
    && result.data["stay"] == "airbnb"
    ){window.location.replace('/iceland');

  }else{
    window.location.replace('/')
  }

});


var widget = {
    name: "imagepicker",
    isFit : function(question) { return question["renderAs"] === 'imagepicker'; },
    isDefaultRender: true,
    afterRender: function(question, el) {

        var $el = $(el).find("select");

        var options = $el.find('option');
        for (var i=1; i<options.length; i++) {
            $(options[i]).data("imgSrc", options[i].text);
            options[i].selected = question.value == options[i].value;
        }
        $el.imagepicker({
            hide_select : true,
            show_label  : false,
            selected: function(opts) {
                question.value = opts.picker.select[0].value;
            }
        })
    }

        ,
        willUnmount: function(question, el) {
            var $el = $(el).find("select");
            $el.data('picker').destroy();
        }

}

Survey.CustomWidgetCollection.Instance.addCustomWidget(widget);


$("#surveyElement").Survey({
    model: survey
});



window.surveyForceUpdate = function() {
    document.getElementById("surveyElement").innerHTML = "";

    $("#surveyElement").Survey({ model: survey });

}
