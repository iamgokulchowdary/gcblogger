const profileImageInput = document.getElementById('profileImage');
  const profilePreview = document.getElementById('profilePreview');

  profileImageInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        profilePreview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });