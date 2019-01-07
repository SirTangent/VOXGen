function generateVOX() {
  var inc = 0;
  var sounds = [];
  var text = document.getElementById("text").value.toLowerCase().split(" ");

  if (document.getElementById("vox/").checked){
    path_dir = "vox/";
  } else if (document.getElementById("vox2/").checked) {
    path_dir = "vox2/";
  }

  var ext = ".wav";

  for (var i in text) {
    sounds[i] = new Howl({
      src: [path_dir + text[i] + ext],
      onend: function() {
        inc++;
        sounds[inc].play();
      }
    });
  }
/*
  for (var j in sounds) {
    if (j < sounds.length - 1) {
      sounds[i].onend = function() {
        sounds[i+1].play();
      }
    }
  }
  */
  sounds[0].play();
}
