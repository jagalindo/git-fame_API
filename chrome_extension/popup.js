  chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
  function(tabs){
    fetch("https://immense-dusk-28515.herokuapp.com/exec_fame?url="+tabs[0].url).then(r => r.text()).then(result => {
      document.getElementById("placeholder").innerHTML=result
    })

  });  