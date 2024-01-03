package utils

import (
	"C"

	WAProto "github.com/krypton-byte/neonize/defproto"
	"github.com/krypton-byte/neonize/neonize"
	"go.mau.fi/whatsmeow"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
	"google.golang.org/protobuf/proto"
)

// Function
func EncodeUploadResponse(response whatsmeow.UploadResponse) *neonize.UploadResponse {
	return &neonize.UploadResponse{
		Url:           &response.URL,
		DirectPath:    &response.DirectPath,
		Handle:        &response.Handle,
		MediaKey:      response.MediaKey,
		FileEncSHA256: response.FileEncSHA256,
		FileSHA256:    response.FileSHA256,
		FileLength:    proto.Uint32(uint32(response.FileLength)),
	}
}

// types.go
func EncodeJidProto(data types.JID) *neonize.JID {
	return &neonize.JID{
		User:       &data.User,
		RawAgent:   proto.Uint32(uint32(data.RawAgent)),
		Device:     proto.Uint32(uint32(data.Device)),
		Integrator: proto.Uint32(uint32(data.Integrator)),
		Server:     &data.Server,
	}
}
func EncodeGroupName(groupName types.GroupName) *neonize.GroupName {
	return &neonize.GroupName{
		Name:      &groupName.Name,
		NameSetAt: proto.Int64(groupName.NameSetAt.Unix()),
		NameSetBy: EncodeJidProto(groupName.NameSetBy),
	}
}
func EncodeGroupTopic(topic types.GroupTopic) *neonize.GroupTopic {
	return &neonize.GroupTopic{
		Topic:        &topic.Topic,
		TopicID:      &topic.TopicID,
		TopicSetAt:   proto.Int64(topic.TopicSetAt.Unix()),
		TopicSetBy:   EncodeJidProto(topic.TopicSetBy),
		TopicDeleted: &topic.TopicDeleted,
	}
}
func EncodeGroupLocked(locked types.GroupLocked) *neonize.GroupLocked {
	return &neonize.GroupLocked{
		IsLocked: &locked.IsLocked,
	}
}
func EncodeGroupAnnounce(announce types.GroupAnnounce) *neonize.GroupAnnounce {
	return &neonize.GroupAnnounce{
		IsAnnounce:        &announce.IsAnnounce,
		AnnounceVersionID: &announce.AnnounceVersionID,
	}
}
func EncodeGroupEphemeral(ephemeral types.GroupEphemeral) *neonize.GroupEphemeral {
	return &neonize.GroupEphemeral{
		IsEphemeral:       &ephemeral.IsEphemeral,
		DisappearingTimer: &ephemeral.DisappearingTimer,
	}
}
func EncodeGroupIncognito(incognito types.GroupIncognito) *neonize.GroupIncognito {
	return &neonize.GroupIncognito{
		IsIncognito: &incognito.IsIncognito,
	}
}
func EncodeGroupParent(parent types.GroupParent) *neonize.GroupParent {
	return &neonize.GroupParent{
		IsParent:                      &parent.IsParent,
		DefaultMembershipApprovalMode: &parent.DefaultMembershipApprovalMode,
	}
}
func EncodeGroupLinkedParent(linkedParent types.GroupLinkedParent) *neonize.GroupLinkedParent {
	return &neonize.GroupLinkedParent{
		LinkedParentJID: EncodeJidProto(linkedParent.LinkedParentJID),
	}
}
func EncodeGroupIsDefaultSub(isDefaultSub types.GroupIsDefaultSub) *neonize.GroupIsDefaultSub {
	return &neonize.GroupIsDefaultSub{
		IsDefaultSubGroup: &isDefaultSub.IsDefaultSubGroup,
	}
}
func EncodeGroupParticipantAddRequest(addRequest types.GroupParticipantAddRequest) *neonize.GroupParticipantAddRequest {
	return &neonize.GroupParticipantAddRequest{
		Code:       &addRequest.Code,
		Expiration: proto.Float32(float32(addRequest.Expiration.Unix())),
	}
}
func EncodeGroupParticipant(participant types.GroupParticipant) *neonize.GroupParticipant {
	participant_group := neonize.GroupParticipant{
		LID:          EncodeJidProto(participant.LID),
		JID:          EncodeJidProto(participant.JID),
		IsAdmin:      &participant.IsAdmin,
		IsSuperAdmin: &participant.IsSuperAdmin,
		DisplayName:  &participant.DisplayName,
		Error:        proto.Int32(int32(participant.Error)),
	}
	if participant.AddRequest != nil {
		participant_group.AddRequest = EncodeGroupParticipantAddRequest(*participant.AddRequest)
	}
	return &participant_group
}

// send.go
func EncodeGroupInfo(info *types.GroupInfo) *neonize.GroupInfo {
	participants := []*neonize.GroupParticipant{}
	for _, participant := range info.Participants {
		participants = append(participants, EncodeGroupParticipant(participant))
	}
	return &neonize.GroupInfo{
		JID:                  EncodeJidProto(info.JID),
		OwnerJID:             EncodeJidProto(info.OwnerJID),
		GroupName:            EncodeGroupName(info.GroupName),
		GroupTopic:           EncodeGroupTopic(info.GroupTopic),
		GroupLocked:          EncodeGroupLocked(info.GroupLocked),
		GroupAnnounce:        EncodeGroupAnnounce(info.GroupAnnounce),
		GroupEphemeral:       EncodeGroupEphemeral(info.GroupEphemeral),
		GroupIncognito:       EncodeGroupIncognito(info.GroupIncognito),
		GroupParent:          EncodeGroupParent(info.GroupParent),
		GroupLinkedParent:    EncodeGroupLinkedParent(info.GroupLinkedParent),
		GroupIsDefaultSub:    EncodeGroupIsDefaultSub(info.GroupIsDefaultSub),
		GroupCreated:         proto.Float32(float32(info.GroupCreated.Unix())),
		ParticipantVersionID: &info.ParticipantVersionID,
		Participants:         participants,
	}
}

func EncodeMessageDebugTimings(debugTimings whatsmeow.MessageDebugTimings) *neonize.MessageDebugTimings {
	return &neonize.MessageDebugTimings{
		Queue:           proto.Int64(debugTimings.Queue.Nanoseconds()),
		Marshal_:        proto.Int64(debugTimings.Marshal.Nanoseconds()),
		GetParticipants: proto.Int64(debugTimings.GetParticipants.Nanoseconds()),
		GetDevices:      proto.Int64(debugTimings.GetParticipants.Nanoseconds()),
		GroupEncrypt:    proto.Int64(debugTimings.Queue.Nanoseconds()),
		PeerEncrypt:     proto.Int64(debugTimings.PeerEncrypt.Nanoseconds()),
		Send:            proto.Int64(debugTimings.Send.Nanoseconds()),
		Resp:            proto.Int64(debugTimings.Queue.Nanoseconds()),
		Retry:           proto.Int64(debugTimings.Retry.Nanoseconds()),
	}
}
func EncodeSendResponse(sendResponse whatsmeow.SendResponse) *neonize.SendResponse {
	return &neonize.SendResponse{
		Timestamp:    proto.Int64(sendResponse.Timestamp.Unix()),
		ID:           proto.String(sendResponse.ID),
		ServerID:     proto.Int64(int64(sendResponse.ServerID)),
		DebugTimings: EncodeMessageDebugTimings(sendResponse.DebugTimings),
	}
}
func EncodeVerifiedNameCertificate(verifiedNameCertificate *waProto.VerifiedNameCertificate) *WAProto.VerifiedNameCertificate {
	return &WAProto.VerifiedNameCertificate{
		Details:         verifiedNameCertificate.Details,
		Signature:       verifiedNameCertificate.Signature,
		ServerSignature: verifiedNameCertificate.ServerSignature,
	}
}
func EncodeLocalizedName(localizedname *waProto.LocalizedName) *WAProto.LocalizedName {
	return &WAProto.LocalizedName{
		Lg:           localizedname.Lg,
		Lc:           localizedname.Lc,
		VerifiedName: localizedname.VerifiedName,
	}
}
func EncodeVerifiedNameCertificate_Details(details *waProto.VerifiedNameCertificate_Details) *WAProto.VerifiedNameCertificate_Details {
	localizedName := []*WAProto.LocalizedName{}
	for _, localized := range details.LocalizedNames {
		localizedName = append(localizedName, EncodeLocalizedName(localized))
	}
	return &WAProto.VerifiedNameCertificate_Details{
		Serial:         details.Serial,
		Issuer:         details.Issuer,
		VerifiedName:   details.VerifiedName,
		LocalizedNames: localizedName,
		IssueTime:      details.IssueTime,
	}
}
func EncodeVerifiedName(verifiedName *types.VerifiedName) *neonize.VerifiedName {
	return &neonize.VerifiedName{
		Certificate: EncodeVerifiedNameCertificate(verifiedName.Certificate),
		Details:     EncodeVerifiedNameCertificate_Details(verifiedName.Details),
	}
}
func EncodeIsOnWhatsApp(isOnWhatsApp types.IsOnWhatsAppResponse) *neonize.IsOnWhatsAppResponse {
	model := &neonize.IsOnWhatsAppResponse{
		Query: &isOnWhatsApp.Query,
		JID:   EncodeJidProto(isOnWhatsApp.JID),
		IsIn:  &isOnWhatsApp.IsIn,
	}
	if isOnWhatsApp.VerifiedName != nil {
		model.VerifiedName = EncodeVerifiedName(isOnWhatsApp.VerifiedName)
	}
	return model
}