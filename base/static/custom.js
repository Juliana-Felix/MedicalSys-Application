var SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};

django.jQuery(function(){
  django.jQuery('.mask-phone').mask(SPMaskBehavior, spOptions);
  django.jQuery('.mask-cep').mask('00000-000');

  django.jQuery('#patient_form').submit(function(){
    django.jQuery('#patient_form').find(":input[class*='mask-']").unmask();
  })
});