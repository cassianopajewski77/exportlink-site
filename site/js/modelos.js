(function(){
  var d=document.getElementById('modelos');if(!d||!d.showModal)return;
  var img=d.querySelector('.docmodal__img'),tabs=d.querySelectorAll('[data-doc]');
  function pick(b){tabs.forEach(function(t){t.setAttribute('aria-selected',t===b?'true':'false')});img.src=b.getAttribute('data-doc');img.alt=b.getAttribute('data-alt');d.querySelector('.docmodal__view').scrollTop=0;}
  tabs.forEach(function(t){t.addEventListener('click',function(){pick(t)})});
  document.querySelectorAll('[data-open-modelos]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();pick(tabs[0]);d.showModal();})});
  d.querySelector('.docmodal__close').addEventListener('click',function(){d.close()});
  d.addEventListener('click',function(e){if(e.target===d)d.close()});
})();
