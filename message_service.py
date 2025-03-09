from jnius import autoclass, cast

mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
context = mActivity.getApplicationContext()

RingtoneManager = autoclass("android.media.RingtoneManager")
Uri = autoclass("android.net.Uri")
AudioAttributesBuilder = autoclass("android.media.AudioAttributes$Builder")
AudioAttributes = autoclass("android.media.AudioAttributes")
AndroidString = autoclass("java.lang.String")
NotificationManager = autoclass("android.app.NotificationManager")
NotificationChannel = autoclass("android.app.NotificationChannel")
NotificationCompat = autoclass("androidx.core.app.NotificationCompat")
NotificationCompatBuilder = autoclass("androidx.core.app.NotificationCompat$Builder")
NotificationManagerCompat = autoclass("androidx.core.app.NotificationManagerCompat")
func_from = getattr(NotificationManagerCompat, "from")


def create_channel():
    sound = cast(Uri, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
    att = AudioAttributesBuilder()
    att.setUsage(AudioAttributes.USAGE_NOTIFICATION)
    att.setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
    att = cast(AudioAttributes, att.build())

    name = cast("java.lang.CharSequence", AndroidString("Potion Notify"))
    description = AndroidString("")
    global channel_id
    channel_id = AndroidString("1")

    importance = NotificationManager.IMPORTANCE_HIGH

    channel = NotificationChannel(channel_id, name, importance)
    channel.setDescription(description)
    channel.enableLights(True)
    channel.enableVibration(True)
    channel.setSound(sound, att)

    notificationManager = context.getSystemService(NotificationManager)
    notificationManager.createNotificationChannel(channel)


def create_notification():
    sound = cast(Uri, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
    builder = NotificationCompatBuilder(context, channel_id)
    builder.setSmallIcon(context.getApplicationInfo().icon)
    builder.setContentTitle(
        cast("java.lang.CharSequence", AndroidString("Potion TIME!"))
    )
    builder.setContentText(
        cast("java.lang.CharSequence", AndroidString("🤍It\'s Potion Time!!!🤍"))
    )
    builder.setSound(sound)
    builder.setPriority(NotificationCompat.PRIORITY_HIGH)
    builder.setVisibility(NotificationCompat.VISIBILITY_PUBLIC)

    compatmanager = NotificationManagerCompat.func_from(context)
    compatmanager.notify("1", builder.build())