from flask import render_template, redirect, url_for, flash
from app.admin.forms import PhotoForm
from app.models import Photo
from app import db
from flask import render_template, redirect, url_for, flash
from app.admin.forms import VideoForm
from app.models import Video
from app import db

@admin.route('/photos')
def manage_photos():
    photos = Photo.query.all()
    return render_template('admin/manage_photos.html', photos=photos)

@admin.route('/photos/add', methods=['GET', 'POST'])
def add_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        photo = Photo(
            title=form.title.data,
            file_path=f"static/images/{form.file.data.filename}",
            description=form.description.data
        )
        db.session.add(photo)
        db.session.commit()
        flash('Photo added successfully!', 'success')
        return redirect(url_for('admin.manage_photos'))
    return render_template('admin/add_photo.html', form=form)

@admin.route('/photos/delete/<int:id>', methods=['POST'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    flash('Photo deleted successfully!', 'success')
    return redirect(url_for('admin.manage_photos'))
# Route to list all videos
@admin.route('/videos')
def manage_videos():
    videos = Video.query.all()
    return render_template('admin/manage_videos.html', videos=videos)

# Route to add a new video
@admin.route('/videos/add', methods=['GET', 'POST'])
def add_video():
    form = VideoForm()
    if form.validate_on_submit():
        # Process the form and save video details to the database
        video = Video(
            title=form.title.data,
            file_path=f"static/videos/{form.file.data.filename}"  # Store file path for the video
        )
        db.session.add(video)
        db.session.commit()
        flash('Video added successfully!', 'success')
        return redirect(url_for('admin.manage_videos'))
    return render_template('admin/add_video.html', form=form)

# Route to delete a video
@admin.route('/videos/delete/<int:id>', methods=['POST'])
def delete_video(id):
    video = Video.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash('Video deleted successfully!', 'success')
    return redirect(url_for('admin.manage_videos'))