from flask import Flask, jsonify

app = Flask(__name__)

#Example of json to retrieve from GET
# here we use the status of MiR robot
status = {
  "joystick_low_speed_mode_enabled": False,
  "mission_queue_url": None,
  "mode_id": 7,
  "moved": 17105.1,
  "mission_queue_id": None,
  "robot_name": "MiR250_Alascom2020",
  "joystick_web_session_id": "",
  "uptime": 633,
  "errors": [],
  "unloaded_map_changes": False,
  "distance_to_next_target": 0,
  "serial_number": "204603004",
  "mode_key_state": "auto",
  "battery_percentage": 54,
  "map_id": "83101853-2597-11eb-aaed-00012979a834",
  "safety_system_muted": False,
  "mission_text": "Cameras are ready to stream",
  "state_text": "EmergencyStop",
  "velocity": {
    "linear": 0,
    "angular": 0
  },
  "footprint": "[[0.54,-0.38],[0.54,0.38],[-0.54,0.38],[-0.54,-0.38]]",
  "user_prompt": None,
  "allowed_methods": None,
  "robot_model": "MiR250",
  "mode_text": "Mission",
  "session_id": "e45f09d4-fd95-11ea-8dc0-00012979a834",
  "state_id": 10,
  "battery_time_remaining": 41080,
  "position": {
    "y": 27.141904830932617,
    "x": 23.356794357299805,
    "orientation": 108.80146026611328
  }
}

#choose the path and the type of request for the method
@app.route("/status", methods=["GET"])
def getStatus():
	return jsonify(status)

if __name__ == '__main__':
	app.run(host='your.ip',port=8081)